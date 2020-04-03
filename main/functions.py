def handle_uploaded_image(f):
    with open('media/event1/images/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def handle_uploaded_file(f):
    with open('media/event1/documentation'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
