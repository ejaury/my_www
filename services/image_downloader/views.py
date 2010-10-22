from django.shortcuts import render_to_response
from django.template import RequestContext
from image_downloader.forms import ImageDownloaderForm

def index(request):
  if request.method == 'POST':
    form = ImageDownloaderForm(request.POST)
    if form.is_valid():
      url = form.cleaned_data['url']
      # launch scraper here
  else:
    form = ImageDownloaderForm()

  return render_to_response('image_downloader/index.html', {
                              'form': form,
                            },
                            context_instance=RequestContext(request))
