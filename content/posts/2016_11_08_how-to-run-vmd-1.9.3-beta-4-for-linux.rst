How to run VMD 1.9.3 beta 4 for Linux
#####################################

:date: 2016-11-8 20:59
:tags:
:category:
:slug: how-to-run-vmd-1.9.3-beta-4-for-linux
:status: published


.. role:: bash(code)
   :language: bash

.. PELICAN_BEGIN_SUMMARY

`VMD <http://www.ks.uiuc.edu/Research/vmd/>`_ is, without any doubt, one of the most used free molecular visualizers out there. The only problem this software has is that the guys of the T&CB group at the university of Illinois do not update it very often. We must be happy then that a new beta version has landed the last 28th of October.

.. PELICAN_END_SUMMARY 

The problem of beta versions is that, well, they are beta. Beta versions are considered to be unstable and contain unknown bugs that users can discover and report. Isn't it fun?

In this case, a minor error avoids some users from enjoying this marvelous software. In order to install it in a 64 bit Linux machine, just download the proper tar.gz file (e.g. *LINUX\_64\ OpenGL,\ CUDA,\ OptiX,\ OSPRay*), unzip it wherever you want, enter the folder and run ./configure with the options you want (running it without options will print them). To be honest, I do not really know if the options you choose will modify the final result. This is an example:

.. code-block:: bash

    > tar -xvf vmd-1.9.3beta4.bin.LINUXAMD64-CUDA8-OptiX4-OSPRay111.opengl.tar.gz
    > cd vmd-1.9.3beta4/
    > ./configure LINUXAMD64 OPENGL LIBTACHYON TCL PYTHON PTHREADS NUMPY
    > cd src
    > sudo make install 

and we are done! Just run :bash:`vmd` in a console emulator and you can start enjo... wait! what happened!

.. code-block:: bash

    > vmd  
    /usr/local/bin/vmd: 331: /usr/local/bin/vmd: Syntax error: "else" unexpected (expecting "then")

Ok, so this is one of these unknown bugs I mentioned before. However, we are lucky that this one is quite simple. A quick inspection of the vmd launcher script (you can find the file using :bash:`which vmd`) reveals that a :bash:`then` statement is missing (after line 329): 

.. code-block:: bash
    :linenostart: 323
    :linenos: table
    
    # Test to see if a 64-bit version of VMD exists
    # in the installation directory, and use the 64-bit
    # version if it is there.
    if [ -x "${VMDDIR}/${vmdbasename}_LINUXPPC64LE" ]
    then
        ARCH=LINUXPPC64LE
    elif [ -x "${VMDDIR}/${vmdbasename}_OPENPOWER" ]
        ARCH=OPENPOWER
    else                                                                                                    
        ARCH=SUMMIT
    fi

Just add the missing :bash:`then` statement, and it will finally work.

.. code-block:: bash
    :linenostart: 323
    :linenos: table
    :hl_lines: 8
    
    # Test to see if a 64-bit version of VMD exists
    # in the installation directory, and use the 64-bit
    # version if it is there.
    if [ -x "${VMDDIR}/${vmdbasename}_LINUXPPC64LE" ]
    then
        ARCH=LINUXPPC64LE
    elif [ -x "${VMDDIR}/${vmdbasename}_OPENPOWER" ]
    then
        ARCH=OPENPOWER
    else                                                                                                    
        ARCH=SUMMIT
    fi

Hope it helps!




