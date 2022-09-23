import re

from django.db.models import Q


def camel_to_snake(variable_name):
    variable_name = re.sub(r"(?<!^)(?=[A-Z])", "_", variable_name).lower()
    return variable_name



class ModelFilterTODO:
    def filter_fields(self, model, filter_fields):
        for fields in filter_fields:
            fld_name = fields.split("=")[0]
            fld_value = fields.split("=")[1]
            if fld_name == "title":
                model = model.filter(title__icontains=fld_value)
            if fld_name == "category":
                model = model.filter(category=fld_value)
            if fld_name == "due_date":
                model = model.filter(due_date=fld_value)
        return model

    def search(self, model, query_string):
        search = query_string["search"]
        if search:
            model = model.filter(
                Q(title__icontains=search)
                | Q(category__icontains=search)
                | Q(due_date__icontains=search)
            )
        return model


