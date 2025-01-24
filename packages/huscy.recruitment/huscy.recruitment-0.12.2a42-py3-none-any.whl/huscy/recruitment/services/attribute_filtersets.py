from datetime import date, timedelta
from functools import reduce

from django.db.models import Q

from huscy.attributes.models import AttributeSet
from huscy.pseudonyms.services import get_subjects as get_subjects_by_pseudonym


def apply_recruitment_criteria(recruitment_criteria):
    filtered_attribute_sets = filter_attributesets_by_attribute_filterset(recruitment_criteria)
    pseudonyms = [attribute_set.pseudonym for attribute_set in filtered_attribute_sets]
    pre_filtered_subjects = get_subjects_by_pseudonym(pseudonyms)
    matching_subjects = filter_subjects_by_age(pre_filtered_subjects, recruitment_criteria)
    return (matching_subjects.select_related('contact')
                             .prefetch_related('legal_representatives'))


def filter_attributesets_by_attribute_filterset(recruitment_criteria):
    queryset = Q()
    for path, condition in recruitment_criteria.attribute_filterset.items():
        queryset &= reduce(
            lambda result, value: extend_queryset(result, path, condition, value),
            condition['values'],
            Q()
        )
    return AttributeSet.objects.filter(queryset)


def extend_queryset(queryset, path, condition, value):
    if condition["operator"] == 'not':
        return queryset | ~Q(**{f'attributes__{path}': value})
    return queryset | Q(**{f'attributes__{path}__{condition["operator"]}': value})


def filter_subjects_by_age(subjects, recruitment_criteria):
    today = date.today()
    min_age = today - timedelta(days=recruitment_criteria.minimum_age_in_months*30)
    max_age = today - timedelta(days=recruitment_criteria.maximum_age_in_months*30)
    return subjects.filter(contact__date_of_birth__lte=min_age, contact__date_of_birth__gte=max_age)


# TODO: remove the lines above for stable version
'''
import operator

def apply_recruitment_criteria(recruitment_criteria, include_children=False):
    attribute_sets = _filter_attributesets_by_filterset(recruitment_criteria)
    matching_subjects = get_subjects_by_pseudonym([attribute_set.pseudonym
                                                   for attribute_set in attribute_sets])
    not_invited_matching_subjects = _exclude_invited_subjects(matching_subjects,
                                                              recruitment_criteria)

    return not_invited_matching_subjects.intersection(get_subjects(include_children))


def _get_filters(attribute_filterset):
    attribute_schema = get_attribute_schema()

    for attribute_name, filter_values in attribute_filterset.items():
        exclude = False

        if attribute_name.startswith('-'):
            attribute_name = attribute_name[1:]
            exclude = True

        attribute_type = _get_attribute_type(attribute_schema.schema, attribute_name)

        if attribute_type in ['integer', 'number']:
            lookup = f'attributes__{attribute_name}__range'
        elif attribute_type == 'array':
            lookup = f'attributes__{attribute_name}__contains'
        else:
            lookup = f'attributes__{attribute_name}'

        q = reduce(operator.or_, (Q(**{lookup: filter_value}) for filter_value in filter_values))

        if exclude:
            q = ~Q(q)

        yield q


def _exclude_invited_subjects(subjects, recruitment_criteria):
    experiment = recruitment_criteria.subject_group.experiment
    participation_request_pseudonyms = ParticipationRequest.objects.filter(
        recruitment_criteria__subject_group__experiment=experiment,
        status=ParticipationRequest.STATUS.get_value('invited')
    ).values_list('pseudonym', flat=True)
    return subjects.exclude(pseudonym__in=participation_request_pseudonyms)
'''
