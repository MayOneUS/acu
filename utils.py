import csv
from functools import partial
from django.db.models import FieldDoesNotExist

from django.http import HttpResponse
from django.utils.text import capfirst


# The following functions were lifted from a Python 2 project.
# TODO: make sure they work with Python 3.4 and Django 1.7, or replace with something simpler.


def csv_response(filename, table):
    """Return a CSV file of the given table as an HttpResponse.

    Args:
        filename: the name of the downloaded CSV file. The extension will be
            '.csv'. This parameter is inserted directly to the response's
            Content-Disposition, and must be escaped accordingly.
        table: a 2-dimensional iterable, in row-major order.
    Returns:
        A CSV HttpResponse with appropriate content_type and
        Content-Disposition.
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="%s.csv"' % filename
    writer = csv.writer(response)
    for row in table:
        # Convert generators to lists for use by writer.writerow.
        writer.writerow(list(row))
    return response


def getattr_chain(obj, name_chain, suppress_attr_errors=False, sep='__'):
    """Apply getattr successively to a chain of attribute names.

    Argument 'name_chain' is a string containing sequence of attribute names
    to look up, starting with the initial object 'obj' and progressing through
    the chain. By default, a double underscore ('__') is expected to separate
    attribute names (as in Django's admin config and queryset keyword args), but
    any string may be specified in argument 'sep'. If 'sep' is None, argument
    'name_chain' is instead expected to be an already-separated iterable of
    attribute names.

    When evaluating a chain of attributes such as 'foo__bar__baz', in some cases
    'bar' may sometimes be None, such as in database models with nullable
    foreign keys. In order to simplify the process of attempting to look up such
    values, argument 'suppress_attr_errors' may be given: if it is True, any
    AttributeErrors raised by lookups on None (e.g., 'None.baz') will be caught,
    and the value None will be returned instead. (Attempted lookups of invalid
    names will still raise errors as usual.) Be aware, though, that specifying
    this option will result in the same behavior whether 'bar' or 'baz' is None.

    Note that while Django's uses of such string-specified attribute lookups are
    limited to database relations, this function performs just as well with
    regular object attributes, and even with properties.

    If a more complex lookup involving function calls or other logic is desired,
    consider a lambda function, such as `lambda obj: obj.foo.bar.baz.qux()`.

    Args:
        obj: the object start the attribute lookup from.
        name_chain: a string containing a sequence of attribute names, separated
            by the value of argument 'sep'. May instead be an iterable of
            attribute names if 'sep' is None.
        suppress_attr_errors: if True, catches AttributeErrors raised from an
            attempted lookup on a None value anywhere in the attribute chain,
            and returns None instead of raising the exception.
        sep: the delimiting characters between the consecutive attribute names
            in argument 'name_chain'. Default is '__', but may be any string.
            If None, 'name_chain' is expected to be an iterable sequence of
            names, rather than a single string.
    Returns:
        The evaluation of the consecutive lookup of attributes in 'name_chain'.

    Example usage:
        >>> class Obj(object): pass
        >>> obj, obj.foo = Obj(), Obj()

        >>> obj.foo.bar = None
        >>> getattr_chain(obj, 'foo__bar')
        >>> # None returned.
        >>> getattr_chain(obj, 'foo__bar__baz')
        Traceback (most recent call last):
            ...
        AttributeError: 'NoneType' object has no attribute 'baz'
        >>> getattr_chain(obj, 'foo__bar__baz', suppress_attr_errors=True)
        >>> # None returned; no exception raised.

        >>> obj.foo.bar = 'spam'
        >>> getattr_chain(obj, 'foo__bar')
        'spam'
        >>> getattr_chain(obj, 'foo__bar__baz')
        Traceback (most recent call last):
            ...
        AttributeError: 'str' object has no attribute 'baz'
        >>> getattr_chain(obj, 'foo__bar__baz', suppress_attr_errors=True)
        Traceback (most recent call last):
            ...
        AttributeError: 'str' object has no attribute 'baz'
        >>> # Only AttributeErrors from NoneType are suppressed.
    """
    names = name_chain if sep is None else name_chain.split(sep)

    for name in names:
        try:
            obj = getattr(obj, name)
        # TODO: consider catching ObjectDoesNotExist as well.
        except AttributeError:
            if suppress_attr_errors and obj is None:
                return None
            else:
                # If suppress_attr_errors is not set, or if the error
                # was due to an invalid field name (rather than a valid
                # field having the value None), re-raise this exception.
                raise
    return obj


def generate_basic_table(columns, data):
    """Generate a table of functions applied to data objects.

    Argument 'columns' is an iterable of 2-tuples of the form (title, function),
    where 'title' is the column title and 'function' is a single-parameter
    function that will be applied to each data element to create the column.

    Returns a 2-dimensional row-major-ordered generator. The first row is the
    column titles; subsequent rows are evaluated functions of the data points.

    Args:
        columns: an iterable of pairs (title, function):
            title: the string to appear at the top of the column.
            function: a callable to be applied to each datum in the column.
        data: a QuerySet, list, or other iterable of arbitrary objects that can
            be passed to the provided functions.
    Yields:
        rows of the table:
            first row: the given column titles.
            subsequent rows: the given column functions applied to each datum.

    Example usage:
        >>> columns = [('Numbers', lambda x: x), ('Squares', lambda x: x ** 2)]
        >>> data = [1, 2, 3, 4, 5]
        >>> list(list(row) for row in generate_basic_table(columns, data))
        [['Numbers', 'Squares'], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25]]
    """
    titles, functions = zip(*columns)
    yield titles
    for obj in data:
        yield (f(obj) for f in functions)  # One row of the table.


def generate_table(columns, data, model=None, capitalize_title=True,
                   remove_nones=False, **kwargs):
    """Wrapper around generate_basic_table with fancier column specifications.

    Argument 'columns' is an iterable of specifications for table columns.
    Each specification is in one of three forms:
        - a tuple (title, func), where 'title' is the column title and 'func'
            is a function that will be applied to each datum in the column.
            Specifications in this format will be passed through unchanged.
        - a tuple (title, attr). The column function will be a lookup of the
            provided attribute, which may be a model field, an ordinary object
            attribute, or a property.
        - a string, which is an attribute name as specified above. If the
            attribute is a model field and the 'model' arg is given, this
            column's title will be the model's verbose_name; otherwise,
            the title will be the string, with single and double underscores
            converted to single spaces.

    See also getattr_chain, which this function uses to look up attributes
    given by the latter two types of column specifications. Any keyword args
    are passed through to it.

    Args:
        columns: an iterable of column specifications.
        model: the model to look up field names from. Only used to get verbose
            field names for column titles, and not used at all if all column
            specifications include titles.
        capitalize_title: if True (the default), derived column names will have
            their first letter capitalized.
        remove_nones: if True, 'None' results from column functions will be
            replaced with the empty string.
        kwargs: passed through to function 'getattr_chain'.
    Yields:
        Column specifications in the form (title, func).

    Example usage:
        def scholarship_report_view(request):
            table = generate_table([
                'id',
                'parent',
                ('Submission Date', 'submission_date'),
                ('Email Address', Scholarship.get_user_email),
                ('Random Numbers', lambda _: random.random()),
            ], data=Scholarship.objects.all(), model=Scholarship)
            return csv_response('Scholarship Information', table)
    """
    def filter_nones(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result if result is not None else ''
        return wrapper

    def converted_columns():
        """Convert column specifications to an identical format."""
        for column in columns:
            # First, figure out whether this column specification is a single
            # string or a tuple (title, spec).
            if type(column) == str:
                if column == '__str__':
                    title = model._meta.verbose_name
                else:
                    # This column is an attribute name.
                    try:
                        # If this attribute is a model field,
                        # retrieve its verbose_name from the model.
                        title = model._meta.get_field(column).verbose_name
                    except (AttributeError, FieldDoesNotExist):
                        # If no model was specified or no such field was found,
                        # fall back on the attribute name, with underscores
                        # (single or double) replaced with (single) spaces.
                        title = column.replace('__', ' ').replace('_', ' ')
                if capitalize_title:
                    title = capfirst(title)
                spec = column
            else:
                title, spec = column
            # Now figure out what to do with the spec.
            if type(spec) == str:
                if spec == '__str__':
                    func = str
                else:
                    # Assume this spec is an attribute name.
                    # Replace it with a function to get that attribute.
                    func = partial(getattr_chain, name_chain=spec, **kwargs)
            else:
                # Assume this spec is a ready-to-go function.
                func = spec
            if remove_nones:
                func = filter_nones(func)
            yield (title, func)

    return generate_basic_table(converted_columns(), data)