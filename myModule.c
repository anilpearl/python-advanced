#include <Python.h>

/*
 * Function to be called from Python
 */
static PyObject* py_printMsg(PyObject* self, PyObject* args)
{
  char *s = "Calling C function from Python!";
  return Py_BuildValue("s", s);
}

/*
 * Another function to be called from Python
 */
static PyObject* py_multiply(PyObject* self, PyObject* args)
{
  double x, y;
  PyArg_ParseTuple(args, "dd", &x, &y);
  return Py_BuildValue("d", x*y);
}

/*
 * Bind Python function names to our C functions
 */
static PyMethodDef myModule_methods[] = {
  {"py_printMsg", py_printMsg, METH_VARARGS},
  {"py_multiply", py_multiply, METH_VARARGS},
  {NULL, NULL}
};

/*
 * Python calls this to let us initialize our module
 */
void initmyModule()
{
  (void) Py_InitModule("myModule", myModule_methods);
}