from app.configuration.routes.routes import *

from app.internal.routers import user, currency

__routes__ = Routes(routers=(user.router, currency.router))

