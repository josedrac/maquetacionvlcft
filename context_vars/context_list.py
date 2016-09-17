import context_vars.index as index
import context_vars.known as known
import context_vars.support as support
import context_vars.supermarket as supermarket
import context_vars.tips as tips
import context_vars.press as press
import context_vars.pets as pets
import context_vars.model as model

def get_context_list():
    return [
        ('index.html', index.get_vars),
        ('known.html', known.get_vars),
        ('support.html', support.get_vars),
        ('supermarket.html', supermarket.get_vars),
        ('tips.html', tips.get_vars),
        ('press.html', press.get_vars),
        ('pets.html', pets.get_vars),
        ('model.html', model.get_vars)
    ]
