from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import TemplateDoesNotExist, loader, Context
from django.contrib.auth.decorators import login_required

from pgweb.util.decorators import ssl_required
from pgweb.util.contexts import NavContext
from pgweb.util.helpers import simple_form

from models import NewsArticle
from forms import NewsArticleForm

def archive(request, paging=None):
	news = NewsArticle.objects.filter(approved=True)
	return render_to_response('news/newsarchive.html', {
		'news': news,
	}, NavContext(request, 'about'))

def item(request, itemid, throwaway=None):
	news = get_object_or_404(NewsArticle, pk=itemid)
	if not news.approved:
		raise Http404
	return render_to_response('news/item.html', {
		'obj': news,
	}, NavContext(request, 'about'))

@ssl_required
@login_required
def form(request, itemid):
	return simple_form(NewsArticle, itemid, request, NewsArticleForm,
					   redirect='/account/edit/news/')

