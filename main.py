def task_manager():
    total_tasks = 0
    tasks_done = 0
    task_list = []

    def add_task(task_description):
        nonlocal total_tasks, tasks_done, task_list
        total_tasks += 1
        task_list.append({'description': task_description, 'completed': False})

        if total_tasks == 1:
            print(
                f"Task '{task_description}' added successfully! \n - There is a total of {total_tasks} task."
            )
        else:
            print(
                f"Task '{task_description}' added successfully! \n - There is a total of {total_tasks} tasks."
            )

    def finish_task(task_description):
        nonlocal tasks_done
        for task in task_list:
            if task['description'] == task_description and not task[
                    'completed']:
                task['completed'] = True
                tasks_done += 1
                print(f"\nTask '{task_description}' marked as completed!")
                print(f" - A total of '{tasks_done}' task(s) were completed!\n")
                break
        else:
            print(f"Task '{task_description}' not found or already completed!\n")

    def list_tasks():
        print("\nTasks:")
        for task in task_list:
            status = "Completed" if task['completed'] else "Not Completed"
            print(f"    - {task['description']} - [{status}]")

    def show_status():
        print(
            f"\nStatus:\n    - Total tasks: {total_tasks},\n    - Finished tasks: {tasks_done},\n    - Not done tasks: {total_tasks - tasks_done}"
        )

    return {
        'add': add_task,
        'finish': finish_task,
        'list': list_tasks,
        'status': show_status
    }


# Exemplo de uso da aplicação
manage = task_manager()

# Adicionando tarefas
manage['add']('Study')
manage['add']('Exercise')
manage['add']('Cook')
manage['list']()
manage['status']()

manage['finish']('Study')
manage['finish']('Cook')

manage['list']()
manage['status']()
