__author__ = 'harvey'

from django.http import HttpResponse, Http404
from django.template import Template, Context
from django.shortcuts import render_to_response

import datetime

def hello(request):
    #print request
    return HttpResponse("Hello World")


def current_datetime(request):
    now = datetime.datetime.now()
    #html = "<html><body> it is now %s.</body></html>" % now
    #return HttpResponse(html)
    return render_to_response('current_datetime.html', {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError as err:
        print "Error:{0}".format(err)
        return Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #html = "<html><body> In %s hours(s), it will be %s. </body></html>" % (offset, dt)
    #return HttpResponse(html)
    return render_to_response('hours_ahead.html', {'hour_offset':offset, 'next_time':dt})

def template_example(request):
    raw_template = """
     <html>
     <head><title>My Template Example</title></head>
     <body>

     {% if  item_list %}
        <p> the list is not empty, let us generate  </p>
     {% else %}
        <p> nothing to generate </p>
     {% endif %}

     <p>My names are</p>
     <ul>
        {% for item in item_list %}
            <li> {{forloop.counter}}: {{ item }} </li>
        {% endfor %}
     </ul>

     <p>my First name is {{item_list.0}} </p>
     <p>my Second name is {{item_list.1}} </p>
     <p>my Last name is {{item_list.2}} </p>
     </body>
     </html>
    """
    t = Template(raw_template)
    item_list = ['harvey', 'dave', 'daclan']
    c = Context({'item_list':item_list})
    return HttpResponse(t.render(c))


def herald_sample_view(request):
    now = datetime.datetime.now()
    return render_to_response('theHerald.html')


