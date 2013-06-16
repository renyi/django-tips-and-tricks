##########################
# LABS SETTINGS          #
##########################
# Developer's playground #
# Play at ur own risk    #
##########################

if LABS_ENABLED and not "sis.labs" in INSTALLED_APPS:
    from .installed_plugins_list import installed_plugins_list

    TEMPLATE_CONTEXT_PROCESSORS += [
        "sis.context_processors.sis_labs"
    ]

    # Loads all modules from sis.plugins
    for plugin in installed_plugins_list('plugins'):
        INSTALLED_APPS.insert(0, "sis.plugins.%s" % plugin)

    # Loads all modules from sis.labs.ui
    for plugin in installed_plugins_list('labs/ui'):
        INSTALLED_APPS.insert(0, "sis.labs.ui.%s" % plugin)

    # Loads all modules from sis.labs.apps
    INSTALLED_APPS.append('sis.labs')
    for plugin in installed_plugins_list('labs/app'):
        INSTALLED_APPS.append(0, "sis.labs.app.%s" % plugin)