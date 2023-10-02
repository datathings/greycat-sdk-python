#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdint.h>

typedef struct
{
  PyObject_HEAD
      int64_t x;
} i64_t;

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

static PyObject *i64_add(i64_t *self, i64_t *other)
{
  i64_t *new = (i64_t *)self->ob_base.ob_type->tp_alloc(self->ob_base.ob_type, 0);
  new->x = self->x + other->x;
  return (PyObject *)new;
}

static PyMethodDef i64_methods[] = {
    {"__add__", (PyCFunction)i64_add, METH_VARARGS, ""},
    {NULL},
};

static PyObject *i64_repr(i64_t *self, PyObject *Py_UNUSED(ignored))
{
  return PyUnicode_FromFormat("%ld", self->x);
}

static PyNumberMethods i64NumberMethods = {
    .nb_add = i64_add,
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
  if (PyType_Ready(&i64Type) < 0)
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

  return m;
}
