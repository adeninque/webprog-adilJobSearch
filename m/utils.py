
menu = [
  {"path": "home", "name": "Home"},
  {"path": "projects", "name": "Projects"},
]

my_projects = [
  {'id': 1, 'title': 'first project', 'body': 'this is my first project'},
  {'id': 2, 'title': 'second project', 'body': 'this is my second project'},
  {'id': 3, 'title': 'third project', 'body': 'this is my third project'},
  {'id': 4, 'title': 'fourth project', 'body': 'this is my fourth project'},
]

def get_user_context(**kwargs):
  context = kwargs
  context.update({
    'menu': menu
  })
  return context