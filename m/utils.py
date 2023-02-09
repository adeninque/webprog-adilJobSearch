
menu = [
  {"path": "home", "name": "Home"},
  {"path": "projects", "name": "Projects"},
]

def get_user_context(**kwargs):
  context = kwargs
  context.update({
    'menu': menu
  })
  return context