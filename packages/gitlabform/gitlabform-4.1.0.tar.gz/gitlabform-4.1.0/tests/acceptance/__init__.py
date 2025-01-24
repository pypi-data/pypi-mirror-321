import os
import random
import string
import textwrap
from contextlib import contextmanager
from typing import List, Union, TYPE_CHECKING

import gitlab
from gitlab.v4.objects import Group, Project
from xkcdpass import xkcd_password as xp

from gitlabform import GitLabForm

CONFIG = """
config_version: 3
"""

DEFAULT_README = "Default README content."

# automate reading files created by run_gitlab_in_docker.sh to run tests in PyCharm / IntelliJ
# (workaround for lack of this feature: https://youtrack.jetbrains.com/issue/PY-5543 )

env_vars_to_files = {
    "GITLAB_URL": "gitlab_url.txt",
    "GITLAB_TOKEN": "gitlab_token.txt",
}

for env_var in env_vars_to_files.keys():
    if env_var not in os.environ:
        print(f"{env_var} not set - trying to read it from a file...")
        for up_dir_level in range(0, 4):
            file_path = (up_dir_level * "../") + env_vars_to_files[env_var]
            print(f"Trying to read {file_path} ...")
            if os.path.isfile(file_path):
                try:
                    with open(file_path) as file:
                        os.environ[env_var] = file.read().strip()
                        print(f"{env_var} set!")
                        break
                except Exception as e:
                    print(f"Failed to read {file_path}: {e}")
            else:
                print(f"{file_path} doesn't exist.")

gl = gitlab.Gitlab(
    os.getenv("GITLAB_URL"), private_token=os.getenv("GITLAB_TOKEN"), per_page=100
)


@contextmanager
def allowed_codes(codes: Union[int, List[int]]):
    """
    A context manager that allows failures on specific response status codes
    when gitlab.Gitlab objects.
    """
    if isinstance(codes, int):
        codes = [codes]

    try:
        yield
    except (gitlab.GitlabHttpError, gitlab.GitlabOperationError) as e:
        if e.response_code not in codes:
            raise e


def get_random_name(entity: str) -> str:
    random_suffix = get_random_suffix()
    return f"gitlabform_{entity}_{random_suffix}"


word_file = xp.locate_wordfile()
my_words = xp.generate_wordlist(wordfile=word_file, min_length=5, max_length=8)


def get_random_suffix():
    return xp.generate_xkcdpassword(wordlist=my_words, numwords=1, delimiter="_")


def get_random_password():
    # copied from Ayushi Rawat's article
    # https://medium.com/analytics-vidhya/create-a-random-password-generator-using-python-2fea485e9da9

    length = 16
    all_chars = string.ascii_letters + string.digits
    password = "".join(random.sample(all_chars, length))

    return password


def create_group(group_name, parent_id=None) -> Group:
    with allowed_codes(404):
        group = gl.groups.create(
            {
                "name": group_name,
                "path": group_name,
                "parent_id": parent_id,
                "visibility": "internal",
            }
        )
    if TYPE_CHECKING:
        assert isinstance(group, Group)
    return group


def create_groups(group_base_name, no_of_groups):
    groups = []
    for group_no in range(1, no_of_groups + 1):
        group_name = group_base_name + str(group_no)
        try:
            group = gl.groups.get(group_name)
        except gitlab.GitlabGetError:
            group = create_group(group_name)
        groups.append(group)
    return groups


def delete_groups(group_base_name, no_of_groups):
    for group_no in range(1, no_of_groups + 1):
        group_name = group_base_name + str(group_no)
        with allowed_codes(404):
            gl.groups.delete(group_name)


def create_project(group: Group, project_name) -> Project:
    project = gl.projects.create(
        {
            "name": project_name,
            "path": project_name,
            "namespace_id": group.id,
            "default_branch": "main",
        }
    )

    project.files.create(
        {
            "branch": "main",
            "file_path": "README.md",
            "content": DEFAULT_README,
            "commit_message": "Create README",
        }
    )
    if TYPE_CHECKING:
        assert isinstance(project, Project)
    return project


def create_users(user_base_name, no_of_users):
    users = []
    for user_no in range(1, no_of_users + 1):
        username = user_base_name + str(user_no)
        existing = gl.users.list(username=username)
        try:
            user = existing[0]
        except IndexError:
            user = gl.users.create(
                {
                    "username": username,
                    "email": username + "@example.com",
                    "name": username + " Example",
                    "password": get_random_password(),
                }
            )
        users.append(user)
    return users


def get_only_branch_access_levels(project: Project, branch):
    protected_branch = None

    with allowed_codes(404):
        protected_branch = project.protectedbranches.get(branch)

    if not protected_branch:
        return None, None, None, None, None, None, None

    push_access_levels = set()
    merge_access_levels = set()
    push_access_user_ids = set()
    merge_access_user_ids = set()
    push_access_group_ids = set()
    merge_access_group_ids = set()
    unprotect_access_level = None

    if "push_access_levels" in protected_branch.attributes:
        for push_access in protected_branch.push_access_levels:
            if not push_access["user_id"] and not push_access["group_id"]:
                push_access_levels.add(push_access["access_level"])
            elif push_access["user_id"]:
                push_access_user_ids.add(push_access["user_id"])
            elif push_access["group_id"]:
                push_access_group_ids.add(push_access["group_id"])

    if "merge_access_levels" in protected_branch.attributes:
        for merge_access in protected_branch.merge_access_levels:
            if not merge_access["user_id"] and not merge_access["group_id"]:
                merge_access_levels.add(merge_access["access_level"])
            elif merge_access["user_id"]:
                merge_access_user_ids.add(merge_access["user_id"])
            elif merge_access["group_id"]:
                merge_access_group_ids.add(merge_access["group_id"])

    if (
        "unprotect_access_levels" in protected_branch.attributes
        and len(protected_branch.unprotect_access_levels) == 1
    ):
        unprotect_access_level = protected_branch.unprotect_access_levels[0][
            "access_level"
        ]

    return (
        sorted(push_access_levels),
        sorted(merge_access_levels),
        sorted(push_access_user_ids),
        sorted(merge_access_user_ids),
        sorted(push_access_group_ids),
        sorted(merge_access_group_ids),
        unprotect_access_level,
    )


def get_only_tag_access_levels(project: Project, tag):
    protected_tag = None

    with allowed_codes(404):
        protected_tag = project.protectedtags.get(tag)

    if not protected_tag:
        return None, None, None

    allowed_to_create_access_levels = set()
    allowed_to_create_access_user_ids = set()
    allowed_to_create_access_group_ids = set()

    tag_details = protected_tag.attributes

    if "create_access_levels" in tag_details:
        for create_access in tag_details["create_access_levels"]:
            if create_access["user_id"]:
                allowed_to_create_access_user_ids.add(create_access["user_id"])

            if create_access["group_id"]:
                allowed_to_create_access_group_ids.add(create_access["group_id"])

            if not create_access["user_id"] and not create_access["group_id"]:
                allowed_to_create_access_levels.add(create_access["access_level"])

    return (
        sorted(allowed_to_create_access_levels),
        sorted(allowed_to_create_access_user_ids),
        sorted(allowed_to_create_access_group_ids),
    )


def get_only_environment_access_levels(project: Project, environment):
    """
    Retrieve details of a given protected environments so that
    tests can easily validate those accordingly.
    TODO: Should also return details about `required_approvals`
    and `group_inheritance_type` for each
    access levels or approval rules.
    """
    protected_environment = None

    with allowed_codes(404):
        protected_environment = project.protected_environments.get(environment)

    if not protected_environment:
        return None, None, None, None, None, None, None

    deploy_access_levels = set()
    deploy_access_user_ids = set()
    deploy_access_group_ids = set()
    approval_rules_access_levels = set()
    approval_rules_user_ids = set()
    approval_rules_group_ids = set()
    required_approval_count = 0

    if "deploy_access_levels" in protected_environment.attributes:
        for deploy_access in protected_environment.deploy_access_levels:
            if not deploy_access["user_id"] and not deploy_access["group_id"]:
                deploy_access_levels.add(deploy_access["access_level"])
            elif deploy_access["user_id"]:
                deploy_access_user_ids.add(deploy_access["user_id"])
            elif deploy_access["group_id"]:
                deploy_access_group_ids.add(deploy_access["group_id"])

    if "approval_rules" in protected_environment.attributes:
        for approval_rules in protected_environment.approval_rules:
            if not approval_rules["user_id"] and not approval_rules["group_id"]:
                approval_rules_access_levels.add(approval_rules["access_level"])
            elif approval_rules["user_id"]:
                approval_rules_user_ids.add(approval_rules["user_id"])
            elif approval_rules["group_id"]:
                approval_rules_group_ids.add(approval_rules["group_id"])

    return (
        sorted(deploy_access_levels),
        sorted(deploy_access_user_ids),
        sorted(deploy_access_group_ids),
        sorted(approval_rules_access_levels),
        sorted(approval_rules_user_ids),
        sorted(approval_rules_group_ids),
        required_approval_count,
    )


def randomize_case(input: str) -> str:
    return "".join(random.choice((str.upper, str.lower))(char) for char in input)


def run_gitlabform(
    config,
    target,
    include_archived_projects=True,
    noop=False,
    output_file=None,
    recurse_subgroups=True,
):
    # f-strings with """ used as configs have the disadvantage of having indentation in them - let's remove it here
    config = textwrap.dedent(config)

    # we don't want to repeat ourselves in the tests, so prefix the configs with this mandatory part here
    config = CONFIG + config

    # allow passing in gitlab RESTObjects. assume full path string otherwise
    if isinstance(target, Group):
        target = target.full_path
    elif isinstance(target, Project):
        target = target.path_with_namespace

    gf = GitLabForm(
        include_archived_projects=include_archived_projects,
        config_string=config,
        target=target,
        noop=noop,
        output_file=output_file,
        recurse_subgroups=recurse_subgroups,
    )
    gf.run()
