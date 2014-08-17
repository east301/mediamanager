from django.contrib import admin


def model_admin(model_cls):
    """
    Registers model admin for the specified model class.

    :param model_cls: model class
    """

    def register_model_admin(model_admin_cls):
        admin.site.register(model_cls, model_admin_cls)
        return model_admin_cls

    return register_model_admin
