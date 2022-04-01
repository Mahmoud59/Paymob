import csv
import io

from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle

from analytics.models import Analysis
from analytics.serializers import AnalysisSerializer


def index(request):
    analytics_data = Analysis.objects.all()
    return render(request, 'analytics/index.html',
                  {'analytics_data': analytics_data})


@api_view(["POST"])
@throttle_classes([UserRateThrottle])
def upload_file_data(request):
    analytics_data_file = request.FILES.get('analytics_file', None)
    if not analytics_data_file.name.endswith('.csv'):
        return Response({"message": "You must upload a CSV file"},
                        status=status.HTTP_400_BAD_REQUEST)

    data_set = analytics_data_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    analytics_data = []
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        analytics_data.append({
            "key": column[0],
            "value": column[1] if column[1] else None
        })

    analysis_serializer = AnalysisSerializer(data=analytics_data, many=True)
    analysis_serializer.is_valid(raise_exception=True)
    analysis_serializer.save()
    return HttpResponseRedirect('/analytics/index/')


@api_view(["POST"])
def similar(request):
    analysis_value = get_object_or_404(
        Analysis, key=request.POST.get("csv_key", None))

    analysis_data = Analysis.objects.exclude(pk=analysis_value.pk)
    repeated_data = []
    not_repeated_data = {}
    value_words = analysis_value.value.split()
    analysis_value_len = len(value_words)

    for word in value_words:
        analysis_has_word = analysis_data.filter(value__icontains=word)
        for row in analysis_has_word:
            if row.pk in not_repeated_data.keys():
                not_repeated_data[row.pk] += 1
            else:
                not_repeated_data[row.pk] = 1

        repeated_data.extend(analysis_has_word)

    for key, value in not_repeated_data.items():
        not_repeated_data[key] = 100 * (
                not_repeated_data[key] / analysis_value_len)

    analysis_has_key = list(set(repeated_data))
    for new_row in analysis_has_key:
        new_row.percentage = not_repeated_data[new_row.pk]

    return render(request, 'analytics/index.html',
                  {'original_key': analysis_value.key,
                   'analytics_similar_data': analysis_has_key})
