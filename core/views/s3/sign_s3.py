import os
import boto3
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class SignS3View(LoginRequiredMixin, View):
    def get(self, request):
        S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')

        file_name = request.GET.get('file_name')
        file_type = request.GET.get('file_type')

        s3_client = boto3.client('s3')

        presigned_post = s3_client.generate_presigned_post(
            Bucket=S3_BUCKET_NAME,
            Key=file_name,
            Fields={"acl": "public-read", "Content-Type": file_type},
            Conditions=[
                {"acl": "public-read"},
                {"Content-Type": file_type}
            ],
            ExpiresIn=3600
        )

        return JsonResponse({
            'data': presigned_post,
            'url': 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET_NAME, file_name)
        })
