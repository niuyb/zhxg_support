
from django.urls import re_path, path

from xman import views

urlpatterns = [
    # re_path(r'^user/list$', views.user_list, name="user_list"),
    # re_path(r'^user/list/api$', views.user_list_api, name="user_list_api"),
    # re_path(r'^user$', views.user_detail, name="user_detail"),
    # re_path(r'^user/info/api$', views.user_info_api, name="user_info_api"),
    # re_path(r'^user/add$', views.add_user, name="add_user"),
    # re_path(r'^user/change$', views.change_user, name="change_user"),
    # re_path(r'^user/delete$', views.delete_user, name="delete_user"),

    re_path(r'^user/list$', views.UserListView.as_view(), name="user_list"),
    re_path(r'^user/detail$', views.user_detail, name="user_detail"),
    re_path(r'^user$', views.UserView.as_view(), name="user"),
    re_path(r'^user/data_node$', views.data_node, name="data_node"),

    re_path(r'^perm/list$', views.PermListView.as_view(), name="perm_list"),
    re_path(r'^perm$', views.PermView.as_view(), name="perm_detail"),
    re_path(r'^perm/info/api$', views.perm_info_api, name="perm_info_api"),
    re_path(r'^perm/tree$', views.perm_tree, name="perm_tree"),
    re_path(r'^perm/tree/api$', views.perm_tree_api, name="perm_tree_api"),
    re_path(r'^pure/perm/tree/api$', views.pure_perm_tree_api, name="pure_perm_tree_api"),
    re_path(r'^perm/list/api$', views.perm_list_api, name="perm_list_api"),
    # re_path(r'^perms/users$', views.get_users_by_perms, name="get_users_by_perms"),
    
    # re_path(r'^group/list$', views.group_list, name="group_list"),
    # re_path(r'^group/list/api$', views.group_list_api, name="group_list_api"),
    # re_path(r'^group$', views.group_detail, name="group_detail"),
    # re_path(r'^group/add$', views.add_group, name="add_group"),
    # re_path(r'^group/change$', views.change_group, name="change_group"),
    # re_path(r'^group/delete$', views.delete_group, name="delete_group"),
    # re_path(r'^group/info/api$', views.group_info_api, name="group_info_api"),
    # re_path(r'^groups/users$', views.get_users_by_groups, name="get_users_by_groups"),

    re_path(r'^role/list$', views.RoleListView.as_view(), name="role_list"),
    re_path(r'^role/detail$', views.role_detail, name="role_detail"),
    re_path(r'^role$', views.RoleView.as_view(), name="role"),

    re_path(r'^module/tree$', views.module_tree, name="module_tree"),
    re_path(r'^module/tree/api$', views.module_tree_api, name="module_tree_api"),
    re_path(r'^module/tree/all/api$', views.module_tree_all_api, name="module_tree_all_api"),
    re_path(r'^module$', views.ModuleView.as_view(), name="module"),
    re_path(r'^module/info/api$', views.module_info_api, name="module_info_api"),
    re_path(r'^module/list$', views.module_list, name="module_list"),
    re_path(r'^module/list/api$', views.module_list_api, name="module_list_api"),
    re_path(r'^module/permissions/list/api$', views.module_permissions_list_api, name="module_permissions_list_api"),
]

app_name = "xman"
