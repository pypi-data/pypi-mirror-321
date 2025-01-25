require(['base/js/namespace', 'base/js/events'], function(IPython, events) {
    events.on('kernel_ready.Kernel', function() {
        IPython.notebook.kernel.execute('%load_ext jupyter_cell_modifier');
    });
});