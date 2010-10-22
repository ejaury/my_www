from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from image_downloader.forms import ImageDownloaderForm
import os
import subprocess as sub
import settings

def index(request):
  if request.method == 'POST':
    form = ImageDownloaderForm(request.POST)
    if form.is_valid():
      url = form.cleaned_data['url']
      project_dir = getattr(settings, 'PROJECT_DIR')
      cmd = 'python %s/libs/tw_image_scraper/scrapy-ctl.py crawl --nolog %s' % \
        (project_dir, url) 
      p = sub.Popen(cmd, shell=True, stdout=sub.PIPE, stderr=sub.PIPE)
      output, err = p.communicate()
      output = output.strip()
      if output and os.path.exists(output):
        zipname = _zip_dir(output)
        f = open(zipname, 'r')
        response = HttpResponse(FileWrapper(f), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename=%s' % \
          os.path.basename(zipname)
        return response
      else:
        form._errors['url'] = \
          form.error_class(['Something went wrong. Cannot process your '\
                            'request. Check the URL/link to make sure that it '\
                            'points to the page with all the pictures '\
                            'you want to download'])
        return render_to_response('image_downloader/index.html', {
                                    'form': form,
                                  },
                                  context_instance=RequestContext(request))
  else:
    form = ImageDownloaderForm()

  return render_to_response('image_downloader/index.html', {
                              'form': form,
                            },
                            context_instance=RequestContext(request))

def _zip_dir(target_dir):
  import zipfile, tempfile
  zipname = os.path.basename(target_dir.strip('/'))
  zip_fullname = os.path.join(tempfile.gettempdir(), zipname) + '.zip'

  # credit:
  # http://stackoverflow.com/questions/3612094/better-way-to-zip-files-in-python-zip-a-whole-directory-with-a-single-command/3612455#3612455
  zip = zipfile.ZipFile(zip_fullname, 'w', zipfile.ZIP_DEFLATED)
  rootlen = len(target_dir) + 1
  for base, dirs, files in os.walk(target_dir):
     for file in files:
        fn = os.path.join(base, file)
        zip.write(fn, fn[rootlen:])
  zip.close()

  return zip_fullname
