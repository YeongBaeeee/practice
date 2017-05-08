import re

from django import forms
from django.conf import settings  # django/conf/global_settings.py + askdjango/settings.py 가 합쳐져서 로드됨
from django.template.loader import render_to_string


class NaverMapPointWidget(forms.TextInput):
    BASE_LAT, BASE_LNG = '37.5336013', '126.9018744'  # 당산역

    def render(self, name, value, attrs):
        width = str(self.attrs.get('width', 800))  # 있으면 가져오고 없으면 800
        height = str(self.attrs.get('height', 600))
        if width.isdigit(): width += 'px'  # 숫자로만 구성되어 있음?
        if height.isdigit(): height += 'px'
        context = {
            'naver_client_id': settings.NAVER_CLIENT_ID,
            'id': attrs['id'],
            'width': width,
            'height': height,
            'base_lng': self.BASE_LNG,
            'base_lat': self.BASE_LAT,
        }
        if value:
            try:
                lng, lat = re.findall(r'[+-]?[\d\.]+', value)
                context.update({'base_lat': lat, 'base_lng': lng})
            except (IndexError, ValueError):
                pass
        html = render_to_string('widgets/NaverMapPointWidget.html', context)
        attrs['readonly'] = 'readonly'
        parent_html = super().render(name, value, attrs)

        return parent_html + html
