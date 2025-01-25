require(['base/js/namespace', 'base/js/events'], function(IPython, events) {
    events.on('kernel_ready.Kernel', function() {
        console.log('Loading jupyter_cell_modifier extension...');
        IPython.notebook.kernel.execute('%load_ext jupyter_cell_modifier');
    });
});
