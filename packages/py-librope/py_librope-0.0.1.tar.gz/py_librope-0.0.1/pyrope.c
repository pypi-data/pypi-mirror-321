#include <Python.h>
#define ROPE_WCHAR 1
#include "rope.h"

typedef struct {
    PyObject_HEAD
    rope *rope;
} PyRope;

static PyObject* PyRope_New(PyTypeObject *type, PyObject *args, PyObject *kwds) {
    PyRope* self = (PyRope*)type->tp_alloc(type, 0);
    if (!self || !(self->rope = rope_new()))
        return NULL;
    const char *str = NULL;
    if (!PyArg_ParseTuple(args, "s", &str)) {
        Py_DECREF(self);
        return NULL;
    }
    rope_insert(self->rope, 0, str);
    return (PyObject*)self;
}

static void PyRope_Dealloc(PyRope* self) {
    if (self->rope)
        rope_free(self->rope);
    Py_TYPE(self)->tp_free((PyObject*)self);
}

static PyObject* PyRope_String(PyRope *self) {
    uint8_t *utf8 = rope_create_cstr(self->rope);
    if (!utf8)
        return NULL;
    PyObject *result = PyUnicode_FromStringAndSize(utf8, rope_char_count(self->rope));
    free(utf8);
    return result;
}

static Py_ssize_t PyRope_length(PyRope *self) {
    return (Py_ssize_t)rope_char_count(self->rope);
}

static PyObject* PyRope_insert(PyRope *self, PyObject *args) {
    int position;
    const char *string;
    if (!PyArg_ParseTuple(args, "is", &position, &string))
        return NULL;
    ROPE_RESULT result = rope_insert(self->rope, position, string);
    if (result == ROPE_OK) {
        Py_RETURN_TRUE;
    } else {
        Py_RETURN_FALSE;
    }
}

static PyObject* PyRope_delete(PyRope *self, PyObject *args) {
    int start;
    int count;
    if (!PyArg_ParseTuple(args, "ii", &start, &count))
        return NULL;
    rope_del(self->rope, start, count);
    Py_RETURN_NONE;
}

static PyMethodDef PyRope_methods[] = {
    {"insert", (PyCFunction)PyRope_insert, METH_VARARGS, NULL},
    {"delete", (PyCFunction)PyRope_delete, METH_VARARGS, NULL},
    {NULL, NULL, 0, NULL}
};

static PyMappingMethods PyRope_mapping = {
    (lenfunc)PyRope_length, NULL, NULL
};

static PyTypeObject PyRopeType = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    "pyrope.PyRope",                            /* tp_name */
    sizeof(PyRope),                             /* tp_basicsize */
    0,                                          /* tp_itemsize */
    (destructor)PyRope_Dealloc,                 /* tp_dealloc */
    0,                                          /* tp_vectorcall_offset */
    0,                                          /* tp_getattr */
    0,                                          /* tp_setattr */
    0,                                          /* tp_as_async */
    0,                                          /* tp_repr */
    0,                                          /* tp_as_number */
    0,                                          /* tp_as_sequence */
    &PyRope_mapping,                            /* tp_as_mapping */
    0,                                          /* tp_hash */
    0,                                          /* tp_call */
    (reprfunc)PyRope_String,                    /* tp_str */
    0,                                          /* tp_getattro */
    0,                                          /* tp_setattro */
    0,                                          /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT,                         /* tp_flags */
    PyDoc_STR("PyRope object"),                 /* tp_doc */
    0,                                          /* tp_traverse */
    0,                                          /* tp_clear */
    0,                                          /* tp_richcompare */
    0,                                          /* tp_weaklistoffset */
    0,                                          /* tp_iter */
    0,                                          /* tp_iternext */
    PyRope_methods,                             /* tp_methods */
    0,                                          /* tp_members */
    0,                                          /* tp_getset */
    0,                                          /* tp_base */
    0,                                          /* tp_dict */
    0,                                          /* tp_descr_get */
    0,                                          /* tp_descr_set */
    0,                                          /* tp_dictoffset */
    0,                                          /* tp_init */
    0,                                          /* tp_alloc */
    (newfunc)PyRope_New,                        /* tp_new */
    0,                                          /* tp_free */
    0,                                          /* tp_is_gc */
    0,                                          /* tp_bases */
    0,                                          /* tp_mro */
    0,                                          /* tp_cache */
    0,                                          /* tp_subclasses */
    0,                                          /* tp_weaklist */
    0,                                          /* tp_del */
    0,                                          /* tp_version_tag */
    0,                                          /* tp_finalize */
    0,                                          /* tp_vectorcall */
    0,                                          /* tp_watched */
};

static PyMethodDef empty_methods[] = {
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef pyrope_module = {
    PyModuleDef_HEAD_INIT,
    "pyrope",
    "Python bindings for librope",
    -1,
    empty_methods
};

PyMODINIT_FUNC PyInit_pyrope(void) {
    if (PyType_Ready(&PyRopeType) < 0)
        return NULL;
    PyObject *m = PyModule_Create(&pyrope_module);
    if (!m)
        return NULL;
    Py_INCREF(&PyRopeType);
    if (PyModule_AddObject(m, "PyRope", (PyObject*)&PyRopeType) < 0) {
        Py_DECREF(&PyRopeType);
        Py_DECREF(m);
        return NULL;
    }
    return m;
}
