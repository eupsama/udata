# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask import request, url_for, redirect, current_app
from mongoengine.queryset.visitor import Q

from udata import search, theme
from udata.models import Dataset, Organization, Reuse, GeoZone
from udata.utils import multi_to_dict
from udata.features.territories import check_for_territories
from udata.i18n import I18nBlueprint

blueprint = I18nBlueprint('search', __name__)

# Maps template variables names to model types
MAPPING = {
    'datasets': Dataset,
    'reuses': Reuse,
    'organizations': Organization,
}


@blueprint.route('/search/', endpoint='index')
def render_search():
    params = multi_to_dict(request.args)

    levels = current_app.config.get('HANDLED_LEVELS')

    geo = GeoZone.objects(
        Q(name__iexact=params.get('q')) &
        Q(level__in=levels)
    ).order_by('-population', '-area').first()

    if geo:
        return redirect(url_for('territories.territory', territory=geo))

    params['facets'] = True
    # We only fetch relevant data for the given filter.
    if 'tag' in params:
        types = ['datasets', 'reuses']
    elif 'badge' in params:
        types = ['datasets', 'organizations']
    else:
        types = ['datasets', 'reuses', 'organizations']
    models = [MAPPING[typ] for typ in types]
    results = search.multisearch(*models, **params)
    context = dict(zip(types, results))
    territories = check_for_territories(params.get('q'))
    context['territories'] = territories
    return theme.render('search.html', **context)
