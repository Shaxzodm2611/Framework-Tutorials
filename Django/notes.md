# Apps vs. Project

The dir. in this case tutorial contains the Python package

The app is the actual web application

# Views

In the app directory, i.e: *"Polls"*, views can be added to the self-explanatory views file.

A **view** in Django is: a Python function that process a HTTP request and returns a HTTP response. The controller in the M-V-C pattern. The logic behind what happens when a user visits a URL.

Views (that are to be accessible by the user) must be mapped to a URL configuration. In this case, the URL Conf. file is located in: 
`../tutorial/polls/urls.py`

This URLconf must be added to the projects root URLconf in: `../tutorial/tutorial/urls.py`

From Djangos tutorial:

```
The idea behind include() is to make it easy to plug-and-play URLs. Since polls are in their own URLconf (polls/urls.py), 
they can be placed under “/polls/”, or under “/fun_polls/”, or under “/content/polls/”, or any other path root, and the app will still work.
```

# Interesting Behaviours of the Migrate Function

Estentially *maps* out or rather builds the neccesary DB's for apps located in `../settings.py`

Apps are inherently modular.

Django also auto-creates the database (SQlite3 by default [configurable]), schema can be created in the `../app/models.py` directory

```Python

class Schema(models.Model):
    .
    .
    .
```

# Part 3 - Code

### View & Urls

Takes in Param :: question_id, returns the question_id to a web-page (pretty boring but the url is interesting)

in `\tutorial\polls\urls.py` -> we link the views back to a url: `\polls\question_id\view`

We pass a list of most recently published Question objects back to index.html, we index through the list and return each question_id and pass it on-to /polls/question_id

This calls the detail view: `/polls/#question_id#` because of:

```Python
# @ ../polls/{ question-id }

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.details, name="details"),


# @ 
```

# Part 5 - Generic Views

Abstract away common web-development cases such as: representing .db values

> We use pk instead of the question_id as the base class DetailView requires the primary key to be passed

Each generic view needs to know what object it is acting on