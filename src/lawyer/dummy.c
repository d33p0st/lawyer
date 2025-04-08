/* dummy.c - Just enough to force binary distribution */
#include <Python.h>

static PyMethodDef methods[] = {
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "_dummy",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit__dummy(void) {
    return PyModule_Create(&module);
}