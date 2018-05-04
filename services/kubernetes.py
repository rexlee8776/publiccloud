class K8SService(object):
    @classmethod
    def create_service(cls, name, user):
        pod = Pod(name, user)
        return pod.create()


class Pod(object):
    def __init__(self, name, user):
        self.name = name
        self.user = user

    def create(self):
        return 'https://www.baidu.com'
