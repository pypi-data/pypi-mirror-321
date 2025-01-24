from jira import JIRA


def get_custom_fields(jira):
    all_fields = jira.fields()
    # print(all_fields)
    custom_fields = {}
    for field in all_fields:
        try:
            # print(field)
            if field.get('custom'):
                if field['scope']['project']['id'] == '10559':
                    custom_fields[field['id']] = field['name']
        except:
            continue
    print(custom_fields)
    return custom_fields


if __name__ == '__main__':
    api_key = "ATATT3xFfGF0YeIApQYdm4c671OUkhg5ggVISNgIb0D1Iqpd2dwwunzff98Pc5VQjb74ZN997uXvvxi6LpmNGJx1kW1BLh5AaudMj5RuWTe6uozsGqGpx_QkySeU2HF-JB37kkza9PREOpOSbiDFZxrI0eqYPV9Fe-bJP0RM16V_GSyDPib0wmw=FE3DE2B1"

    # Jira 服务器的 URL
    jira_url = "https://shopline.atlassian.net/"
    # Jira API 密钥
    jira_api_key = api_key
    # Jira 用户名
    jira_user = "lu.lu@shopline.com"

    # 连接到 Jira 服务器
    jira = JIRA(server=jira_url, basic_auth=(jira_user, jira_api_key))

    # 获取一个项目的信息
    project_key = 10559  # 替换为你想要获取的项目的 key
    project = jira.project(project_key)
    print(f"Project: {project.key} - {project.name}")

    all_fields = jira.fields()
    # print(all_fields)

    # 获取项目的问题
    issues = jira.search_issues(f"project={project_key}")
    issue = jira.issue(issues[0])
    # print("Issue Key:", issue.key)
    # print("Summary:", issue.fields.summary)
    # # print("Description:", issue.fields.description)
    # print("Assignee:", issue.fields.assignee.displayName if issue.fields.assignee else "Unassigned")
    # print("Reporter:", issue.fields.reporter.displayName)
    # print("Status:", issue.fields.status.name)
    # print("Priority:", issue.fields.priority.name)
    # print("Created:", issue.fields.created)
    # print("Updated:", issue.fields.updated)
    # print("Due Date:", issue.fields.duedate)
    # print("Labels:", issue.fields.labels)
    # print("Components:", [component.name for component in issue.fields.components])
    # print(issue.fields.__dict__.items())
    custom_fields = get_custom_fields(jira)
    for field_name, field_value in issue.fields.__dict__.items():
        try:
            # if field_name.startswith("customfield_"):
                # continue
            print(f"Custom Field ID: {field_name}, NAME:{custom_fields[field_name]}, Value: {field_value}")
        except:
            continue
