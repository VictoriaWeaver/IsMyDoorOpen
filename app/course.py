class Course():
    """
    Class for the attributes of courses
    """
    def __init__(self, course_num, class_name, time):
        """
        :param course_num: the course number in SIS
        :param class_name: the name of the course
        :param time: the time span for the class

        Initialize the Course
        """

        # TODO add in an attribute for which days of the week the class occurs
        # currently just manually adding in the classes for each day of the week

        self.course_num = course_num
        self.class_name = class_name
        self.time = time
