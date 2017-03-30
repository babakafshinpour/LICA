%module mi

%{
    #define SWIG_FILE_WITH_INIT
    #include <errno.h>
    #include "mi.h"
%}

%include "numpy.i"

%init %{
    import_array();
%}


%exception crop
{
	errno = 0;
	$action
	if (errno != 0)
	{
		switch(errno)
		{
	 	case EPERM:
	 		PyErr_Format(PyExc_IndexError, "Index error");
	 		break;
		case ENOMEM:
			PyErr_Format(PyExc_MemoryError, "Not enough memory");
			break;
		default:
			PyErr_Format(PyExc_Exception, "Unknown exception");
		}
		SWIG_fail;
	}
}

%apply (double* IN_ARRAY2, int DIM1, int DIM2) {(double *rangevec, int n, int c)}
%apply (double* IN_ARRAY2, int DIM1, int DIM2) {(double *inp2, int N, int dim)}
%apply (double** ARGOUTVIEWM_ARRAY2, int* DIM1, int* DIM2) {(double **arr_out, int *dim1_out, int *dim2_out)}

%include "mi.h"