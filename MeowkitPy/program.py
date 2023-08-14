
#from MeowkitPy import app

class WebhookHandler(object):

    def __init__(self, idx: int) -> None:
        self.idx = idx
        self.funcs = {}

    def handle(self, event):
        func = self.funcs.get(event, None)
        if func is None:
            print('No handler of ' + event + ' and no default handler')
        else:
            #print(f'handle-call {self.idx} >> {func}')
            func(event)

    def add(self, event, message=None):
        def decorator(func):
            print(f"obj[{self.idx}] >> {event}:{message} >> {func}")
            self.funcs['MessageEvent'] = func # Obj 同一個事件只能綁一次
            return func
        return decorator

    def param(self, Service):
        def decorator(func):

            return func(Service)
        return decorator

class Service():
    def __init__(self, handler: WebhookHandler, idx: int) -> None:
        self.handler = handler
        self.idx = idx

svc_list = [
    Service(WebhookHandler(0), 0),
    Service(WebhookHandler(1), 1),
]

for svc in svc_list:
    @svc.handler.add('MessageEvent', 'Hello')
    def on_function(event, service=svc):
        print(f"func: {service.idx} >> {event}")


svc0 = svc_list[0]
svc1 = svc_list[1]

svc0.handler.handle('MessageEvent')
svc1.handler.handle('MessageEvent')

if __name__ == '__main__':
    pass