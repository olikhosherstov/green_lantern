from django.shortcuts import render, redirect
from django.views.generic import CreateView
from apps.photos.forms import PhotoForm

# Create your views here.
from apps.photos.models import Photo


class UploadPhotosView(CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'photos/photos_upload.html'

    def get_form_kwargs(self):
        kwargs = super(UploadPhotosView, self).get_form_kwargs()
        kwargs['dealer_id'] = self.request.user.pk
        return kwargs

    def form_valid(self, form):
        form.instance.dealer = self.request.user
        form.save()
        return redirect('success')
