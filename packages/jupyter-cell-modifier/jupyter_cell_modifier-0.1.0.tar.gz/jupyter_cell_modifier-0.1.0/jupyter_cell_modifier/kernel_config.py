def load_jupyter_server_extension(nb_server_app):
    """
    Called when the extension is loaded.
    
    Args:
        nb_server_app (NotebookWebApplication): handle to the Notebook webserver instance.
    """
    try:
        # Get the kernel manager
        kernel_manager = nb_server_app.kernel_manager
        
        # Set kernel manager options for better stability
        kernel_manager.kernel_spec_manager.ensure_native_kernel = True
        kernel_manager.default_kernel_name = 'python3'
        
        # Set longer timeouts
        kernel_manager.start_kernel_timeout = 60
        kernel_manager.shutdown_wait_time = 10.0
        
    except Exception as e:
        nb_server_app.log.error(f"Error loading server extension: {e}")
        raise 