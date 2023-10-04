#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdint.h>

typedef struct
{
  PyObject_HEAD
      int64_t x;
} i64_t;

typedef struct
{
  PyObject_HEAD double x;
} f64_t;

static PyTypeObject i64Type;

static PyTypeObject f64Type;

static int to_int(PyObject *v, int64_t *res)
{
  if (PyLong_Check(v))
  {
    *res = PyLong_AsLong(v);
    return 0;
  }
  if (PyObject_IsInstance(v, &i64Type))
  {
    *res = ((i64_t *)v)->x;
    return 0;
  }
  return 1;
}

static double to_double(PyObject *v, double *res)
{
  if (PyFloat_Check(v))
  {
    *res = PyFloat_AsDouble(v);
    return 0;
  }
  if (PyObject_IsInstance(v, &f64Type))
  {
    *res = ((f64_t *)v)->x;
    return 0;
  }
  if (PyLong_Check(v))
  {
    *res = PyLong_AsDouble(v);
    return 0;
  }
  if (PyObject_IsInstance(v, &i64Type))
  {
    *res = (double)((i64_t *)v)->x;
    return 0;
  }
  return 1;
}

static void i64_dealloc(i64_t *self)
{
  Py_TYPE(self)->tp_free((PyObject *)self);
}

static PyObject *i64_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
  i64_t *self = (i64_t *)type->tp_alloc(type, 0);
  if (self != NULL)
  {
    self->x = 0;
  }
  return (PyObject *)self;
}

static int i64_init(i64_t *self, PyObject *args)
{
  if (!PyArg_ParseTuple(args, "|l", &self->x))
  {
    return -1;
  }

  return 0;
}

static PyObject *i64_add(PyObject *x, PyObject *y)
{
  int64_t i_x, i_y;
  if (0 != to_int(x, &i_x))
  {
    size_t msg_len = 45 + strlen(x->ob_type->tp_name) + strlen(y->ob_type->tp_name);
    char msg[msg_len];
    snprintf(msg, msg_len, "unsupported operand type(s) for +: '%s' and '%s'", x->ob_type->tp_name, y->ob_type->tp_name);
    PyErr_SetString(PyExc_ValueError, msg);
    return NULL;
  }
  if (0 != to_int(y, &i_y))
  {
    size_t msg_len = 45 + strlen(x->ob_type->tp_name) + strlen(y->ob_type->tp_name);
    char msg[msg_len];
    snprintf(msg, msg_len, "unsupported operand type(s) for +: '%s' and '%s'", x->ob_type->tp_name, y->ob_type->tp_name);
    PyErr_SetString(PyExc_ValueError, msg);
    return NULL;
  }
  i64_t *new = (i64_t *)i64Type.tp_alloc(&i64Type, 0);
  if (new != NULL)
  {
    new->x = i_x + i_y;
  }
  return new;
}

static PyObject *i64_subtract(PyObject *x, PyObject *y)
{
  int64_t i_x, i_y;
  if (0 != to_int(x, &i_x))
  {
    size_t msg_len = 45 + strlen(x->ob_type->tp_name) + strlen(y->ob_type->tp_name);
    char msg[msg_len];
    snprintf(msg, msg_len, "unsupported operand type(s) for -: '%s' and '%s'", x->ob_type->tp_name, y->ob_type->tp_name);
    PyErr_SetString(PyExc_ValueError, msg);
    return NULL;
  }
  if (0 != to_int(y, &i_y))
  {
    size_t msg_len = 45 + strlen(x->ob_type->tp_name) + strlen(y->ob_type->tp_name);
    char msg[msg_len];
    snprintf(msg, msg_len, "unsupported operand type(s) for -: '%s' and '%s'", x->ob_type->tp_name, y->ob_type->tp_name);
    PyErr_SetString(PyExc_ValueError, msg);
    return NULL;
  }
  i64_t *new = (i64_t *)i64Type.tp_alloc(&i64Type, 0);
  if (new != NULL)
  {
    new->x = i_x - i_y;
  }
  return new;
}

static PyObject *i64_multiply(PyObject *x, PyObject *y)
{
  int64_t i_x, i_y;
  if (0 != to_int(x, &i_x))
  {
    size_t msg_len = 45 + strlen(x->ob_type->tp_name) + strlen(y->ob_type->tp_name);
    char msg[msg_len];
    snprintf(msg, msg_len, "unsupported operand type(s) for *: '%s' and '%s'", x->ob_type->tp_name, y->ob_type->tp_name);
    PyErr_SetString(PyExc_ValueError, msg);
    return NULL;
  }
  if (0 != to_int(y, &i_y))
  {
    size_t msg_len = 45 + strlen(x->ob_type->tp_name) + strlen(y->ob_type->tp_name);
    char msg[msg_len];
    snprintf(msg, msg_len, "unsupported operand type(s) for *: '%s' and '%s'", x->ob_type->tp_name, y->ob_type->tp_name);
    PyErr_SetString(PyExc_ValueError, msg);
    return NULL;
  }
  i64_t *new = (i64_t *)i64Type.tp_alloc(&i64Type, 0);
  if (new != NULL)
  {
    new->x = i_x *i_y;
  }
  return new;
}

static PyObject *i64_modulo(PyObject *x, PyObject *y)
{
  int64_t i_x, i_y;
  if (0 != to_int(x, &i_x))
  {
    size_t msg_len = 45 + strlen(x->ob_type->tp_name) + strlen(y->ob_type->tp_name);
    char msg[msg_len];
    snprintf(msg, msg_len, "unsupported operand type(s) for %%: '%s' and '%s'", x->ob_type->tp_name, y->ob_type->tp_name);
    PyErr_SetString(PyExc_ValueError, msg);
    return NULL;
  }
  if (0 != to_int(y, &i_y))
  {
    size_t msg_len = 45 + strlen(x->ob_type->tp_name) + strlen(y->ob_type->tp_name);
    char msg[msg_len];
    snprintf(msg, msg_len, "unsupported operand type(s) for %%: '%s' and '%s'", x->ob_type->tp_name, y->ob_type->tp_name);
    PyErr_SetString(PyExc_ValueError, msg);
    return NULL;
  }
  i64_t *new = (i64_t *)i64Type.tp_alloc(&i64Type, 0);
  if (new != NULL)
  {
    new->x = i_x % i_y;
  }
  return new;
}

static PyObject *i64_divmod(PyObject *x, PyObject *y)
{
  int64_t i_x, i_y;
  if (0 != to_int(x, &i_x))
  {
    size_t msg_len = 50 + strlen(x->ob_type->tp_name) + strlen(y->ob_type->tp_name);
    char msg[msg_len];
    snprintf(msg, msg_len, "unsupported operand type(s) for divmod: '%s' and '%s'", x->ob_type->tp_name, y->ob_type->tp_name);
    PyErr_SetString(PyExc_ValueError, msg);
    return NULL;
  }
  if (0 != to_int(y, &i_y))
  {
    size_t msg_len = 50 + strlen(x->ob_type->tp_name) + strlen(y->ob_type->tp_name);
    char msg[msg_len];
    snprintf(msg, msg_len, "unsupported operand type(s) for divmod: '%s' and '%s'", x->ob_type->tp_name, y->ob_type->tp_name);
    PyErr_SetString(PyExc_ValueError, msg);
    return NULL;
  }
  PyObject *tuple = PyTuple_New(2);
  i64_t *div = (i64_t *)i64Type.tp_alloc(&i64Type, 0);
  i64_t *mod = (i64_t *)i64Type.tp_alloc(&i64Type, 0);
  div->x = i_x / i_y;
  mod->x = i_x % i_y;
  PyTuple_SET_ITEM(tuple, 0, div);
  PyTuple_SET_ITEM(tuple, 1, mod);
  return tuple;
}

static PyObject *i64_power(PyObject *x, PyObject *y, PyObject *z)
{
  int64_t i_x, i_y, i_z = 1;
  if (0 != to_int(x, &i_x))
  {
    size_t msg_len = 49 + strlen(x->ob_type->tp_name) + strlen(y->ob_type->tp_name) + strlen(z->ob_type->tp_name);
    char msg[msg_len];
    snprintf(msg, msg_len, "unsupported operand type(s) for +: '%s', '%s' and '%s'", x->ob_type->tp_name, y->ob_type->tp_name, z->ob_type->tp_name);
    PyErr_SetString(PyExc_ValueError, msg);
    return NULL;
  }
  if (0 != to_int(y, &i_y))
  {
    size_t msg_len = 49 + strlen(x->ob_type->tp_name) + strlen(y->ob_type->tp_name) + strlen(z->ob_type->tp_name);
    char msg[msg_len];
    snprintf(msg, msg_len, "unsupported operand type(s) for +: '%s', '%s' and '%s'", x->ob_type->tp_name, y->ob_type->tp_name, z->ob_type->tp_name);
    PyErr_SetString(PyExc_ValueError, msg);
    return NULL;
  }
  if (!Py_IsNone(z))
  {
    if (0 != to_int(z, &i_z))
    {
      return NULL;
    }
  }
  i64_t *new = (i64_t *)i64Type.tp_alloc(&i64Type, 0);
  if (new != NULL)
  {
    new->x = powl(i_x, i_y);
    if (i_z != 1)
    {
      new->x %= i_z;
    }
  }
  return new;
}

static PyObject *i64_negative(i64_t *self)
{
  i64_t *new = (i64_t *)i64Type.tp_alloc(&i64Type, 0);
  if (new != NULL)
  {
    new->x = -self->x;
  }
  return (PyObject *)new;
}

static PyObject *i64_positive(i64_t *self)
{
  i64_t *new = (i64_t *)i64Type.tp_alloc(&i64Type, 0);
  if (new != NULL)
  {
    new->x = self->x;
  }
  return (PyObject *)new;
}

static PyObject *i64_absolute(i64_t *self)
{
  i64_t *new = (i64_t *)i64Type.tp_alloc(&i64Type, 0);
  if (new != NULL)
  {
    new->x = labs(self->x);
  }
  return (PyObject *)new;
}

static int *i64_bool(i64_t *self)
{
  return self->x != 0 ? 1 : 0;
}

static PyObject *i64_invert(i64_t *self)
{
  i64_t *new = (i64_t *)i64Type.tp_alloc(&i64Type, 0);
  if (new != NULL)
  {
    new->x = ~self->x;
  }
  return (PyObject *)new;
}

static PyObject *i64_lshift(PyObject *x, PyObject *y)
{
  int64_t i_x, i_y;
  if (0 != to_int(x, &i_x))
  {
    return NULL;
  }
  if (0 != to_int(y, &i_y))
  {
    return NULL;
  }
  i64_t *new = (i64_t *)i64Type.tp_alloc(&i64Type, 0);
  if (new != NULL)
  {
    new->x = i_x << i_y;
  }
  return new;
}

static PyObject *i64_rshift(PyObject *x, PyObject *y)
{
  int64_t i_x, i_y;
  if (0 != to_int(x, &i_x))
  {
    return NULL;
  }
  if (0 != to_int(y, &i_y))
  {
    return NULL;
  }
  i64_t *new = (i64_t *)i64Type.tp_alloc(&i64Type, 0);
  if (new != NULL)
  {
    new->x = i_x >> i_y;
  }
  return new;
}

static PyObject *i64_and(PyObject *x, PyObject *y)
{
  int64_t i_x, i_y;
  if (0 != to_int(x, &i_x))
  {
    return NULL;
  }
  if (0 != to_int(y, &i_y))
  {
    return NULL;
  }
  i64_t *new = (i64_t *)i64Type.tp_alloc(&i64Type, 0);
  if (new != NULL)
  {
    new->x = i_x &i_y;
  }
  return new;
}

static PyObject *i64_xor(PyObject *x, PyObject *y)
{
  int64_t i_x, i_y;
  if (0 != to_int(x, &i_x))
  {
    return NULL;
  }
  if (0 != to_int(y, &i_y))
  {
    return NULL;
  }
  i64_t *new = (i64_t *)i64Type.tp_alloc(&i64Type, 0);
  if (new != NULL)
  {
    new->x = i_x ^ i_y;
  }
  return new;
}

static PyObject *i64_or(PyObject *x, PyObject *y)
{
  int64_t i_x, i_y;
  if (0 != to_int(x, &i_x))
  {
    return NULL;
  }
  if (0 != to_int(y, &i_y))
  {
    return NULL;
  }
  i64_t *new = (i64_t *)i64Type.tp_alloc(&i64Type, 0);
  if (new != NULL)
  {
    new->x = i_x | i_y;
  }
  return new;
}

static PyObject *i64_int(i64_t *self)
{
  return PyLong_FromLong(self->x);
}

static PyObject *i64_float(i64_t *self)
{
  return PyFloat_FromDouble((double)self->x);
}

static PyObject *i64_divide(PyObject *x, PyObject *y)
{
  int64_t i_x, i_y;
  if (0 != to_int(x, &i_x))
  {
    return NULL;
  }
  if (0 != to_int(y, &i_y))
  {
    return NULL;
  }
  i64_t *new = (i64_t *)i64Type.tp_alloc(&i64Type, 0);
  if (new != NULL)
  {
    new->x = i_x / i_y;
  }
  return new;
}

static PyObject *i64_repr(i64_t *self)
{
  return PyUnicode_FromFormat("%ld", self->x);
}

static void f64_dealloc(f64_t *self)
{
  Py_TYPE(self)->tp_free((PyObject *)self);
}

static PyObject *f64_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
  f64_t *self = (f64_t *)type->tp_alloc(type, 0);
  if (self != NULL)
  {
    self->x = 0.0;
  }
  return (PyObject *)self;
}

static int f64_init(f64_t *self, PyObject *args)
{
  if (!PyArg_ParseTuple(args, "|d", &self->x))
  {
    return -1;
  }
  return 0;
}

static PyObject *f64_add(PyObject *x, PyObject *y)
{
  double d_x, d_y;
  if (0 != to_double(x, &d_x))
  {
    return NULL;
  }
  if (0 != to_double(y, &d_y))
  {
    return NULL;
  }
  f64_t *new = (f64_t *)f64Type.tp_alloc(&f64Type, 0);
  if (new != NULL)
  {
    new->x = d_x + d_y;
  }
  return new;
}

static PyObject *f64_subtract(PyObject *x, PyObject *y)
{
  double d_x, d_y;
  if (0 != to_double(x, &d_x))
  {
    return NULL;
  }
  if (0 != to_double(y, &d_y))
  {
    return NULL;
  }
  f64_t *new = (f64_t *)f64Type.tp_alloc(&f64Type, 0);
  if (new != NULL)
  {
    new->x = d_x - d_y;
  }
  return new;
}

static PyObject *f64_multiply(PyObject *x, PyObject *y)
{
  double d_x, d_y;
  if (0 != to_double(x, &d_x))
  {
    return NULL;
  }
  if (0 != to_double(y, &d_y))
  {
    return NULL;
  }
  f64_t *new = (f64_t *)f64Type.tp_alloc(&f64Type, 0);
  if (new != NULL)
  {
    new->x = d_x *d_y;
  }
  return new;
}

static PyObject *f64_modulo(PyObject *x, PyObject *y)
{
  double d_x, d_y;
  if (0 != to_double(x, &d_x))
  {
    return NULL;
  }
  if (0 != to_double(y, &d_y))
  {
    return NULL;
  }
  f64_t *new = (f64_t *)f64Type.tp_alloc(&f64Type, 0);
  if (new != NULL)
  {
    new->x = fmod(d_x, d_y);
  }
  return new;
}

static PyObject *f64_divmod(PyObject *x, PyObject *y)
{
  double d_x, d_y;
  if (0 != to_double(x, &d_x))
  {
    return NULL;
  }
  if (0 != to_double(y, &d_y))
  {
    return NULL;
  }
  PyObject *tuple = PyTuple_New(2);
  f64_t *div = (f64_t *)f64Type.tp_alloc(&f64Type, 0);
  f64_t *mod = (f64_t *)f64Type.tp_alloc(&f64Type, 0);
  div->x = floor(d_x / d_y);
  mod->x = fmod(d_x, d_y);
  PyTuple_SET_ITEM(tuple, 0, div);
  PyTuple_SET_ITEM(tuple, 1, mod);
  return tuple;
}

static PyObject *f64_power(PyObject *x, PyObject *y, PyObject *z)
{
  double d_x, d_y, d_z = 1.0;
  if (0 != to_double(x, &d_x))
  {
    return NULL;
  }
  if (0 != to_double(y, &d_y))
  {
    return NULL;
  }
  if (!Py_IsNone(z))
  {
    if (0 != to_double(z, &d_z))
    {
      return NULL;
    }
  }
  f64_t *new = (f64_t *)f64Type.tp_alloc(&f64Type, 0);
  if (new != NULL)
  {
    new->x = pow(d_x, d_y);
    if (d_z != 1)
    {
      new->x = fmod(new->x, d_z);
    }
  }
  return new;
}

static PyObject *f64_negative(f64_t *self)
{
  f64_t *new = (f64_t *)f64Type.tp_alloc(&f64Type, 0);
  if (new != NULL)
  {
    new->x = -self->x;
  }
  return new;
}

static PyObject *f64_positive(f64_t *self)
{
  f64_t *new = (f64_t *)f64Type.tp_alloc(&f64Type, 0);
  if (new != NULL)
  {
    new->x = self->x;
  }
  return new;
}

static PyObject *f64_absolute(f64_t *self)
{
  f64_t *new = (f64_t *)f64Type.tp_alloc(&f64Type, 0);
  if (new != NULL)
  {
    new->x = fabs(self->x);
  }
  return new;
}

static int f64_bool(f64_t *self)
{
  return self->x != 0.0 ? 1 : 0;
}

static PyObject *f64_int(f64_t *self)
{
  return PyLong_FromDouble(self->x);
}

static PyObject *f64_float(f64_t *self)
{
  return PyFloat_FromDouble(self->x);
}

static PyObject *f64_floor_divide(PyObject *x, PyObject *y)
{
  double d_x, d_y;
  if (0 != to_double(x, &d_x))
  {
    return NULL;
  }
  if (0 != to_double(y, &d_y))
  {
    return NULL;
  }
  f64_t *new = (f64_t *)f64Type.tp_alloc(&f64Type, 0);
  if (new != NULL)
  {
    new->x = floor(d_x / d_y);
  }
  return new;
}

static PyObject *f64_divide(PyObject *x, PyObject *y)
{
  double d_x, d_y;
  if (0 != to_double(x, &d_x))
  {
    return NULL;
  }
  if (0 != to_double(y, &d_y))
  {
    return NULL;
  }
  f64_t *new = (f64_t *)f64Type.tp_alloc(&f64Type, 0);
  if (new != NULL)
  {
    new->x = d_x / d_y;
  }
  return new;
}

static PyObject *f64_repr(f64_t *self)
{
  return PyUnicode_FromFormat("%R", PyFloat_FromDouble(self->x)); // TODO: decref?
}

static PyNumberMethods i64NumberMethods = {
    .nb_add = i64_add,
    .nb_subtract = i64_subtract,
    .nb_multiply = i64_multiply,
    .nb_remainder = i64_modulo,
    .nb_divmod = i64_divmod,
    .nb_power = i64_power,
    .nb_negative = i64_negative,
    .nb_positive = i64_positive,
    .nb_absolute = i64_absolute,
    .nb_bool = i64_bool,
    .nb_invert = i64_invert,
    .nb_lshift = i64_lshift,
    .nb_rshift = i64_rshift,
    .nb_and = i64_and,
    .nb_xor = i64_xor,
    .nb_or = i64_or,
    .nb_int = i64_int,
    .nb_float = i64_float,

    .nb_inplace_add = i64_add,
    .nb_inplace_subtract = i64_subtract,
    .nb_inplace_multiply = i64_multiply,
    .nb_inplace_remainder = i64_modulo,
    .nb_inplace_lshift = i64_lshift,
    .nb_inplace_rshift = i64_rshift,
    .nb_inplace_and = i64_and,
    .nb_inplace_xor = i64_xor,
    .nb_inplace_or = i64_or,

    .nb_floor_divide = i64_divide,
    .nb_true_divide = f64_divide,
    .nb_inplace_floor_divide = i64_divide,
    .nb_inplace_true_divide = f64_divide,
};

static PyTypeObject i64Type = {
    PyVarObject_HEAD_INIT(NULL, 0).tp_name = "gctypes.i64",
    .tp_doc = PyDoc_STR(""),
    .tp_basicsize = sizeof(i64_t),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = i64_new,
    .tp_init = (initproc)i64_init,
    .tp_dealloc = (destructor)i64_dealloc,
    .tp_repr = i64_repr,
    .tp_as_number = &i64NumberMethods,
};

static PyNumberMethods f64NumberMethods = {
    .nb_add = f64_add,
    .nb_subtract = f64_subtract,
    .nb_multiply = f64_multiply,
    .nb_remainder = f64_modulo,
    .nb_divmod = f64_divmod,
    .nb_power = f64_power,
    .nb_negative = f64_negative,
    .nb_positive = f64_positive,
    .nb_absolute = f64_absolute,
    .nb_bool = f64_bool,
    .nb_int = f64_int,
    .nb_float = f64_float,

    .nb_inplace_add = f64_add,
    .nb_inplace_subtract = f64_subtract,
    .nb_inplace_multiply = f64_multiply,
    .nb_inplace_remainder = f64_modulo,

    .nb_floor_divide = f64_floor_divide,
    .nb_true_divide = f64_divide,
    .nb_inplace_floor_divide = f64_floor_divide,
    .nb_inplace_true_divide = f64_divide,
};

static PyTypeObject f64Type = {
    PyVarObject_HEAD_INIT(NULL, 0).tp_name = "gctypes.f64",
    .tp_doc = PyDoc_STR(""),
    .tp_basicsize = sizeof(f64_t),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = f64_new,
    .tp_init = (initproc)f64_init,
    .tp_dealloc = (destructor)f64_dealloc,
    .tp_repr = f64_repr,
    .tp_as_number = &f64NumberMethods,
};

static PyModuleDef gctypesModule = {
    PyModuleDef_HEAD_INIT,
    .m_name = "gctypes",
    .m_doc = "",
    .m_size = -1,
};

PyMODINIT_FUNC
PyInit_gctypes(void)
{
  PyObject *m;
  if (PyType_Ready(&i64Type) < 0 || PyType_Ready(&f64Type) < 0)
    return NULL;

  m = PyModule_Create(&gctypesModule);
  if (m == NULL)
    return NULL;

  Py_INCREF(&i64Type);
  if (PyModule_AddObject(m, "i64", (PyObject *)&i64Type) < 0)
  {
    Py_DECREF(&i64Type);
    Py_DECREF(m);
    return NULL;
  }

  Py_INCREF(&f64Type);
  if (PyModule_AddObject(m, "f64", (PyObject *)&f64Type) < 0)
  {
    Py_DECREF(&f64Type);
    Py_DECREF(m);
    return NULL;
  }

  return m;
}
