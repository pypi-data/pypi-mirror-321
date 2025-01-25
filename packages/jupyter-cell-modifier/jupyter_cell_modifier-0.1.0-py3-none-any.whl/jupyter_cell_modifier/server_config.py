def load_jupyter_server_extension(nb_server_app):
    """Configure the Jupyter server extension."""
    try:
        web_app = nb_server_app.web_app
        
        # Configure kernel manager
        kernel_manager = nb_server_app.kernel_manager
        kernel_manager.kernel_spec_manager.ensure_native_kernel = True
        kernel_manager.default_kernel_name = 'python3'
        kernel_manager.start_kernel_timeout = 60
        kernel_manager.shutdown_wait_time = 10.0
        
    except Exception as e:
        nb_server_app.log.error(f"Error configuring server extension: {e}")
        raise
