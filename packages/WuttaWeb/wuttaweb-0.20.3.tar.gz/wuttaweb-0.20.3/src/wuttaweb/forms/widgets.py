# -*- coding: utf-8; -*-
################################################################################
#
#  wuttaweb -- Web App for Wutta Framework
#  Copyright © 2024 Lance Edgar
#
#  This file is part of Wutta Framework.
#
#  Wutta Framework is free software: you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation, either version 3 of the License, or (at your option) any
#  later version.
#
#  Wutta Framework is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#
#  You should have received a copy of the GNU General Public License along with
#  Wutta Framework.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
"""
Form widgets

This module defines some custom widgets for use with WuttaWeb.

However for convenience it also makes other Deform widgets available
in the namespace:

* :class:`deform:deform.widget.Widget` (base class)
* :class:`deform:deform.widget.TextInputWidget`
* :class:`deform:deform.widget.TextAreaWidget`
* :class:`deform:deform.widget.PasswordWidget`
* :class:`deform:deform.widget.CheckedPasswordWidget`
* :class:`deform:deform.widget.CheckboxWidget`
* :class:`deform:deform.widget.SelectWidget`
* :class:`deform:deform.widget.CheckboxChoiceWidget`
* :class:`deform:deform.widget.DateTimeInputWidget`
* :class:`deform:deform.widget.MoneyInputWidget`
"""

import datetime
import decimal
import os

import colander
import humanize
from deform.widget import (Widget, TextInputWidget, TextAreaWidget,
                           PasswordWidget, CheckedPasswordWidget,
                           CheckboxWidget, SelectWidget, CheckboxChoiceWidget,
                           DateTimeInputWidget, MoneyInputWidget)
from webhelpers2.html import HTML

from wuttjamaican.conf import parse_list

from wuttaweb.db import Session
from wuttaweb.grids import Grid


class ObjectRefWidget(SelectWidget):
    """
    Widget for use with model "object reference" fields, e.g.  foreign
    key UUID => TargetModel instance.

    While you may create instances of this widget directly, it
    normally happens automatically when schema nodes of the
    :class:`~wuttaweb.forms.schema.ObjectRef` (sub)type are part of
    the form schema; via
    :meth:`~wuttaweb.forms.schema.ObjectRef.widget_maker()`.

    In readonly mode, this renders a ``<span>`` tag around the
    :attr:`model_instance` (converted to string).

    Otherwise it renders a select (dropdown) element allowing user to
    choose from available records.

    This is a subclass of :class:`deform:deform.widget.SelectWidget`
    and uses these Deform templates:

    * ``select``
    * ``readonly/objectref``

    .. attribute:: model_instance

       Reference to the model record instance, i.e. the "far side" of
       the foreign key relationship.

       .. note::

          You do not need to provide the ``model_instance`` when
          constructing the widget.  Rather, it is set automatically
          when the :class:`~wuttaweb.forms.schema.ObjectRef` type
          instance (associated with the node) is serialized.
    """
    readonly_template = 'readonly/objectref'

    def __init__(self, request, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.url = url

    def get_template_values(self, field, cstruct, kw):
        """ """
        values = super().get_template_values(field, cstruct, kw)

        # add url, only if rendering readonly
        readonly = kw.get('readonly', self.readonly)
        if readonly:
            if 'url' not in values and self.url and getattr(field.schema, 'model_instance', None):
                values['url'] = self.url(field.schema.model_instance)

        return values


class NotesWidget(TextAreaWidget):
    """
    Widget for use with "notes" fields.

    In readonly mode, this shows the notes with a background to make
    them stand out a bit more.

    Otherwise it effectively shows a ``<textarea>`` input element.

    This is a subclass of :class:`deform:deform.widget.TextAreaWidget`
    and uses these Deform templates:

    * ``textarea``
    * ``readonly/notes``
    """
    readonly_template = 'readonly/notes'


class WuttaCheckboxChoiceWidget(CheckboxChoiceWidget):
    """
    Custom widget for :class:`python:set` fields.

    This is a subclass of
    :class:`deform:deform.widget.CheckboxChoiceWidget`.

    :param request: Current :term:`request` object.

    It uses these Deform templates:

    * ``checkbox_choice``
    * ``readonly/checkbox_choice``
    """

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.config = self.request.wutta_config
        self.app = self.config.get_app()


class WuttaDateTimeWidget(DateTimeInputWidget):
    """
    Custom widget for :class:`python:datetime.datetime` fields.

    The main purpose of this widget is to leverage
    :meth:`~wuttjamaican:wuttjamaican.app.AppHandler.render_datetime()`
    for the readonly display.

    It is automatically used for SQLAlchemy mapped classes where the
    field maps to a :class:`sqlalchemy:sqlalchemy.types.DateTime`
    column.  For other (non-mapped) datetime fields, you may have to
    use it explicitly via
    :meth:`~wuttaweb.forms.base.Form.set_widget()`.

    This is a subclass of
    :class:`deform:deform.widget.DateTimeInputWidget` and uses these
    Deform templates:

    * ``datetimeinput``
    """

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.config = self.request.wutta_config
        self.app = self.config.get_app()

    def serialize(self, field, cstruct, **kw):
        """ """
        readonly = kw.get('readonly', self.readonly)
        if readonly and cstruct:
            dt = datetime.datetime.fromisoformat(cstruct)
            return self.app.render_datetime(dt)

        return super().serialize(field, cstruct, **kw)


class WuttaMoneyInputWidget(MoneyInputWidget):
    """
    Custom widget for "money" fields.  This is used by default for
    :class:`~wuttaweb.forms.schema.WuttaMoney` type nodes.

    The main purpose of this widget is to leverage
    :meth:`~wuttjamaican:wuttjamaican.app.AppHandler.render_currency()`
    for the readonly display.

    This is a subclass of
    :class:`deform:deform.widget.MoneyInputWidget` and uses these
    Deform templates:

    * ``moneyinput``

    :param request: Current :term:`request` object.

    :param scale: If this kwarg is specified, it will be passed along
       to ``render_currency()`` call.
    """

    def __init__(self, request, *args, **kwargs):
        self.scale = kwargs.pop('scale', 2)
        super().__init__(*args, **kwargs)
        self.request = request
        self.config = self.request.wutta_config
        self.app = self.config.get_app()

    def serialize(self, field, cstruct, **kw):
        """ """
        readonly = kw.get('readonly', self.readonly)
        if readonly:
            if cstruct in (colander.null, None):
                return HTML.tag('span')
            cstruct = decimal.Decimal(cstruct)
            text = self.app.render_currency(cstruct, scale=self.scale)
            return HTML.tag('span', c=[text])

        return super().serialize(field, cstruct, **kw)


class FileDownloadWidget(Widget):
    """
    Widget for use with :class:`~wuttaweb.forms.schema.FileDownload`
    fields.

    This only supports readonly, and shows a hyperlink to download the
    file.  Link text is the filename plus file size.

    This is a subclass of :class:`deform:deform.widget.Widget` and
    uses these Deform templates:

    * ``readonly/filedownload``

    :param request: Current :term:`request` object.

    :param url: Optional URL for hyperlink.  If not specified, file
       name/size is shown with no hyperlink.
    """
    readonly_template = 'readonly/filedownload'

    def __init__(self, request, *args, **kwargs):
        self.url = kwargs.pop('url', None)
        super().__init__(*args, **kwargs)
        self.request = request
        self.config = self.request.wutta_config
        self.app = self.config.get_app()

    def serialize(self, field, cstruct, **kw):
        """ """
        # nb. readonly is the only way this rolls
        kw['readonly'] = True
        template = self.readonly_template

        path = cstruct or None
        if path:
            kw.setdefault('filename', os.path.basename(path))
            kw.setdefault('filesize', self.readable_size(path))
            if self.url:
                kw.setdefault('url', self.url)

        else:
            kw.setdefault('filename', None)
            kw.setdefault('filesize', None)

        kw.setdefault('url', None)
        values = self.get_template_values(field, cstruct, kw)
        return field.renderer(template, **values)

    def readable_size(self, path):
        """ """
        try:
            size = os.path.getsize(path)
        except os.error:
            size = 0
        return humanize.naturalsize(size)


class GridWidget(Widget):
    """
    Widget for fields whose data is represented by a :term:`grid`.

    This is a subclass of :class:`deform:deform.widget.Widget` but
    does not use any Deform templates.

    This widget only supports "readonly" mode, is not editable.  It is
    merely a convenience around the grid itself, which does the heavy
    lifting.

    Instead of creating this widget directly you probably should call
    :meth:`~wuttaweb.forms.base.Form.set_grid()` on your form.

    :param request: Current :term:`request` object.

    :param grid: :class:`~wuttaweb.grids.base.Grid` instance, used to
       display the field data.
    """

    def __init__(self, request, grid, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.grid = grid

    def serialize(self, field, cstruct, **kw):
        """
        This widget simply calls
        :meth:`~wuttaweb.grids.base.Grid.render_table_element()` on
        the ``grid`` to serialize.
        """
        readonly = kw.get('readonly', self.readonly)
        if not readonly:
            raise NotImplementedError("edit not allowed for this widget")

        return self.grid.render_table_element()


class RoleRefsWidget(WuttaCheckboxChoiceWidget):
    """
    Widget for use with User
    :attr:`~wuttjamaican:wuttjamaican.db.model.auth.User.roles` field.
    This is the default widget for the
    :class:`~wuttaweb.forms.schema.RoleRefs` type.

    This is a subclass of :class:`WuttaCheckboxChoiceWidget`.
    """
    readonly_template = 'readonly/rolerefs'

    def serialize(self, field, cstruct, **kw):
        """ """
        model = self.app.model

        # special logic when field is editable
        readonly = kw.get('readonly', self.readonly)
        if not readonly:

            # but does not apply if current user is root
            if not self.request.is_root:
                auth = self.app.get_auth_handler()
                admin = auth.get_role_administrator(self.session)

                # prune admin role from values list; it should not be
                # one of the options since current user is not admin
                values = kw.get('values', self.values)
                values = [val for val in values
                          if val[0] != admin.uuid]
                kw['values'] = values

        else: # readonly

            # roles
            roles = []
            if cstruct:
                for uuid in cstruct:
                    role = self.session.get(model.Role, uuid)
                    if role:
                        roles.append(role)
            kw['roles'] = roles

            # url
            url = lambda role: self.request.route_url('roles.view', uuid=role.uuid)
            kw['url'] = url

        # default logic from here
        return super().serialize(field, cstruct, **kw)


class UserRefsWidget(WuttaCheckboxChoiceWidget):
    """
    Widget for use with Role
    :attr:`~wuttjamaican:wuttjamaican.db.model.auth.Role.users` field.
    This is the default widget for the
    :class:`~wuttaweb.forms.schema.UserRefs` type.

    This is a subclass of :class:`WuttaCheckboxChoiceWidget`; however
    it only supports readonly mode and does not use a template.
    Rather, it generates and renders a
    :class:`~wuttaweb.grids.base.Grid` showing the users list.
    """

    def serialize(self, field, cstruct, **kw):
        """ """
        readonly = kw.get('readonly', self.readonly)
        if not readonly:
            raise NotImplementedError("edit not allowed for this widget")

        model = self.app.model
        columns = ['username', 'active']

        # generate data set for users
        users = []
        if cstruct:
            for uuid in cstruct:
                user = self.session.get(model.User, uuid)
                if user:
                    users.append(dict([(key, getattr(user, key))
                                       for key in columns + ['uuid']]))

        # do not render if no data
        if not users:
            return HTML.tag('span')

        # grid
        grid = Grid(self.request, key='roles.view.users',
                    columns=columns, data=users)

        # view action
        if self.request.has_perm('users.view'):
            url = lambda user, i: self.request.route_url('users.view', uuid=user['uuid'])
            grid.add_action('view', icon='eye', url=url)
            grid.set_link('person')
            grid.set_link('username')

        # edit action
        if self.request.has_perm('users.edit'):
            url = lambda user, i: self.request.route_url('users.edit', uuid=user['uuid'])
            grid.add_action('edit', url=url)

        # render as simple <b-table>
        # nb. must indicate we are a part of this form
        form = getattr(field.parent, 'wutta_form', None)
        return grid.render_table_element(form)


class PermissionsWidget(WuttaCheckboxChoiceWidget):
    """
    Widget for use with Role
    :attr:`~wuttjamaican:wuttjamaican.db.model.auth.Role.permissions`
    field.

    This is a subclass of :class:`WuttaCheckboxChoiceWidget`.  It uses
    these Deform templates:

    * ``permissions``
    * ``readonly/permissions``
    """
    template = 'permissions'
    readonly_template = 'readonly/permissions'

    def serialize(self, field, cstruct, **kw):
        """ """
        kw.setdefault('permissions', self.permissions)

        if 'values' not in kw:
            values = []
            for gkey, group in self.permissions.items():
                for pkey, perm in group['perms'].items():
                    values.append((pkey, perm['label']))
            kw['values'] = values

        return super().serialize(field, cstruct, **kw)


class EmailRecipientsWidget(TextAreaWidget):
    """
    Widget for :term:`email setting` recipient fields (``To``, ``Cc``,
    ``Bcc``).

    This is a subclass of
    :class:`deform:deform.widget.TextAreaWidget`.  It uses these
    Deform templates:

    * ``textarea``
    * ``readonly/email_recips``

    See also the :class:`~wuttaweb.forms.schema.EmailRecipients`
    schema type, which uses this widget.
    """
    readonly_template = 'readonly/email_recips'

    def serialize(self, field, cstruct, **kw):
        """ """
        readonly = kw.get('readonly', self.readonly)
        if readonly:
            kw['recips'] = parse_list(cstruct or '')

        return super().serialize(field, cstruct, **kw)

    def deserialize(self, field, pstruct):
        """ """
        if pstruct is colander.null:
            return colander.null

        values = [value for value in parse_list(pstruct)
                  if value]
        return ', '.join(values)


class BatchIdWidget(Widget):
    """
    Widget for use with the
    :attr:`~wuttjamaican:wuttjamaican.db.model.batch.BatchMixin.id`
    field of a :term:`batch` model.

    This widget is "always" read-only and renders the Batch ID as
    zero-padded 8-char string
    """

    def serialize(self, field, cstruct, **kw):
        """ """
        if cstruct is colander.null:
            return colander.null

        batch_id = int(cstruct)
        return f'{batch_id:08d}'
