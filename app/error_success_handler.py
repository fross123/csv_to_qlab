class ErrorHandler:
    """Handles errors and success messages for CSV to QLab operations"""

    def __init__(self):
        self.errors = []
        self.success = []

    def handle_errors(self, status, message):
        """Record an error message"""
        print("There was an error:")
        print(message)
        self.errors.append({"status": status, "message": message})

    def count_success(self, status, message):
        """Record a success message"""
        self.success.append({"status": status, "message": message})

    def get_errors(self):
        """Return all error messages"""
        return self.errors

    def get_success(self):
        """Return all success messages"""
        return self.success

    def has_errors(self):
        """Check if there are any errors"""
        return len(self.errors) > 0

    def clear(self):
        """Clear all errors and success messages"""
        self.errors.clear()
        self.success.clear()


# Global instance for backward compatibility
_global_handler = ErrorHandler()

# Legacy global lists (for backward compatibility)
errors = _global_handler.errors
success = _global_handler.success


def handle_errors(status, message):
    """Legacy function for backward compatibility"""
    _global_handler.handle_errors(status, message)


def return_errors():
    """Legacy function for backward compatibility"""
    return _global_handler.get_errors()


def count_success(status, message):
    """Legacy function for backward compatibility"""
    _global_handler.count_success(status, message)


def return_success():
    """Legacy function for backward compatibility"""
    return _global_handler.get_success()


def clear_errors_and_success():
    """Legacy function for backward compatibility"""
    _global_handler.clear()
