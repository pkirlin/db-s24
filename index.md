---
layout: home
title: CS 340 - Databases
nav_exclude: true
permalink: /:path/
seo:
  type: Course
  name: CS 340 - Databases
---

# {{ site.tagline }}
{: .mb-2 }
{{ site.description }}
{: .fs-6 .fw-300 }

{% if site.announcements %}
{{ site.announcements.last }}
[Announcements](announcements.md){: .btn .btn-outline .fs-3 }
{% endif %}

## Administrivia
- Instructor: Phillip Kirlin
- Office hours: Mondays 10-11, Tuesdays 12:30-2, Wednesdays 11-12, Thursdays 2-3:30.  Also available by appointment.
- [Canvas page](https://rhodes.instructure.com/courses/6149): Use for grades and online assignment 
submissions. 
- [Syllabus](syllabus/syllabus-db-s24.pdf) and [additional policies](syllabus/additional-policies.pdf).

## Resources

## Calendar
{% for module in site.modules %}
{{ module }}
{% endfor %}

