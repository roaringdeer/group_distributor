import subject

class Timetable:
    def __init__(self, subject_list):
        self.subject_list = subject_list
        self.collision_matrix = {}
        self.create_collision_matrix()

    def create_collision_matrix(self) -> list:
        subject_names = []
        subject_tasks = []
        for subject in self.subject_list:
            for task in subject.task_list:
                for other_subject in self.subject_list:
                    for other_task in other_subject.task_list:
                        if task.day == other_task.day:
                            if other_task.start_hours <= task.start_hours <= other_task.end_hours:
                                if other_task.start_minutes <= task.start_minutes <= other_task.end_minutes:
                                    self.collision_matrix[subject.name][task.name] = 1
                            elif task.start_hours <= other_task.start_hours <= task.end_hours:
                                if task.start_minutes <= other_task.start_minutes <= task.end_minutes:
                                    self.collision_matrix[subject.name][task.name] = 1
                            elif task.start_hours <= other_task.start_hours <= task.end_hours:
                                if task.start_minutes <= other_task.start_minutes <= task.end_minutes:
                                    self.collision_matrix[subject.name][task.name] = 1
                            elif task.start_hours <= other_task.start_hours <= task.end_hours:
                                if task.start_minutes <= other_task.start_minutes <= task.end_minutes:
                                    self.collision_matrix[subject.name][task.name] = 1
        pass