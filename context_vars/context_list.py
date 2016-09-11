import context_vars.index as index
import context_vars.known as known
import context_vars.support as support
import context_vars.supermarket as supermarket
import context_vars.mapsearch as mapsearch
import context_vars.tips as tips
import context_vars.press as press
import context_vars.pets as pets
import context_vars.model as model
import context_vars.committee as committee
import context_vars.jobs as jobs
import context_vars.questions as questions
import context_vars.services as services
import context_vars.contactus as contactus
import context_vars.card as card
import context_vars.invoice as invoice
import context_vars.news as news
import context_vars.inside_tip as inside_tip
import context_vars.detail as detail
import context_vars.history as history
import context_vars.notFound as notFound

def get_context_list():
    return [
        ('index.html', index.get_vars),
        ('known.html', known.get_vars),
        ('support.html', support.get_vars),
        ('supermarket.html', supermarket.get_vars),
        ('map-search.html', mapsearch.get_vars),
        ('tips.html', tips.get_vars),
        ('press.html', press.get_vars),
        ('pets.html', pets.get_vars),
        ('model.html', model.get_vars),
        ('committee.html', committee.get_vars),
        ('jobs.html', jobs.get_vars),
        ('questions.html', questions.get_vars),
        ('services.html', services.get_vars),
        ('contactus.html', contactus.get_vars),
        ('card.html', card.get_vars),
        ('invoice.html', invoice.get_vars),
        ('news.html', news.get_vars),
        ('inside-tip.html', inside_tip.get_vars),
        ('detail.html', detail.get_vars),
        ('history.html', history.get_vars),
        ('404.html', notFound.get_vars)
    ]
