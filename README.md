# Django AI Channels

####  AI in the browser intelligent action on the backend

Django AI Channels adds AI to Django's "batteries included" philosophy. You add the AI model you want to a webpage. The AI model, a neural network, runs in the browser and sends events back to the server over a websocket. A Django channels consumer listens for events and saves them to the database.

## Example: You want to classify objects appearing in a live video feed
Let's say you want to be notified of objects appearing in a video feed.

Create a webpage and add a html video element to capture a stream from a webcam. Use the video_classifier template tag to attach an image classification model to the video element. The image classification model takes a few seconds to load in the browser. It then runs in the browser and each time it recognise an object, a cat wearing sunglasses for example, it will send an event back to the server over a websocket.

The video_classifier template tag needs to know: 
- the id of the element to attach to
- where to send the websocket events

```html
<!DOCTYPE html>
{% load mediapipe %}
<html lang="en">
  <body>
    <video id="webcam" autoplay></video>
    {% video_classifier video_id="webcam" websocket_path='ws/demo/cam0' %}
  </body>
</html>
```

That's it! Each time objects are recognized an event is sent back to the server. vision_classifier events give us the category of object detected along with a confidence score which tells us how certain the AI model is of its guess. A score of one means the model is 100% certain of its guess. Below is an example event.

```json
[
  {
    'categories': 
      [
        {'index': 837, 'score': 0.046875, 'categoryName': 'sunglasses', 'displayName': ''},
        {'index': 836, 'score': 0.04296875, 'categoryName': 'sunglass', 'displayName': ''},
        {'index': 570, 'score': 0.04296875, 'categoryName': 'gasmask', 'displayName': ''}
      ],
    'headIndex': 0,
    'headName': 'probability'
  }
]
```


Events are saved to the `ClassificationEvent` model in the database. You could override the `ClassificationEventConsumer` channels consumer to provide custom processing of events. 


## Install and use
> [!CAUTION]
> not in PyPI yet

Install into environment
```commandline
pip install django-ai-channels
```
Make sure an ASGI server is set up run the Django Channels websocket consumer application.

## Demo app

See the `demo` directory for examples of a django project using the AI models.

To run the demo. Install requirements from the top level of the GitHub repo.
```commandline
pip install -r requirements.txt -r requirements-dev.txt
```

Running the demo
```commandline
cd demo
python manage.py runserver
```

Navigate to the web browser and follow the links for the different AI models.

## Running the tests
> [!CAUTION]
> Tests are broken

From the top level of the GitHub repo
```commandline
python manage.py test
```
