---
sidebar_position: 4
---

# Testing Guide

CSV to QLab uses pytest for testing with comprehensive coverage of the configuration-driven architecture.

## Test Suite Overview

**Total Coverage: 86%**

The test suite includes:
- 50 total tests
- 28 OSC configuration tests
- 17 CSV parsing tests
- 5 integration tests

## Running Tests

### Prerequisites

```bash
# Activate virtual environment
source env/bin/activate

# Install test dependencies
pip install -r requirements.txt
```

### Run All Tests

```bash
# Run all tests
python -m pytest

# Run with verbose output
python -m pytest -v

# Run with coverage report
python -m pytest --cov=app --cov-report=term-missing
```

### Run Specific Test Files

```bash
# OSC configuration tests only
python -m pytest app/tests/test_osc_config.py -v

# CSV parser tests only
python -m pytest app/tests/test_csv_parser.py -v

# Integration tests only
python -m pytest app/tests/test_app.py -v
```

### Run Specific Test Classes or Functions

```bash
# Run specific test class
python -m pytest app/tests/test_osc_config.py::TestDuplicatePropertyNames -v

# Run specific test function
python -m pytest app/tests/test_osc_config.py::TestDuplicatePropertyNames::test_no_duplicate_property_names_global_vs_cue_specific -v
```

## Test Files

### `test_osc_config.py`

Tests for OSC configuration loading and validation.

**Critical Tests:**
- ✅ **Duplicate property name detection** - Prevents silent failures
- ✅ Property validation (ranges, enums, types)
- ✅ Version-specific properties (QLab 4 vs 5)
- ✅ Auto-properties
- ✅ Conditional properties

**Example:**
```python
def test_no_duplicate_property_names_global_vs_cue_specific():
    """Verify no property names overlap between global and cue-specific"""
    # This test prevents configuration errors where the same property
    # name exists in both global_properties and cue_type_properties,
    # which would cause the global property to always win in lookups
```

### `test_csv_parser.py`

Tests for CSV parsing and OSC message generation.

**Covered Areas:**
- CSV parsing and header normalization
- Property processing
- Passcode handling
- Cue type validation
- Edge cases (unicode, special characters)

### `test_app.py`

Integration tests for the Flask application.

**Covered Areas:**
- HTTP endpoints
- File upload handling
- QLab version handling
- Error responses

## Critical Tests Explained

### 1. Duplicate Property Detection

**Why it's critical:** If a property name exists in both `global_properties` and a cue type's properties, the global property always wins. This causes silent failures where cue-specific properties are never used.

**Test Location:** `test_osc_config.py::TestDuplicatePropertyNames`

**What it checks:**
```python
# Fails if any property name appears in both:
global_props = {"level": {...}}
cue_type_props = {"audio": {"level": {...}}}  # CONFLICT!
```

### 2. Property Validation

**Why it's critical:** Invalid values sent to QLab can cause cues to be created with wrong settings.

**Test Location:** `test_osc_config.py::TestPropertyValidation`

**What it checks:**
- Numeric ranges (e.g., `continueMode` must be 0-2)
- Valid values lists (e.g., `color` must be from approved list)
- Type conversion (int, float, bool, string)

### 3. Version Isolation

**Why it's critical:** QLab 4 and 5 have different OSC properties, especially for network cues.

**Test Location:** `test_osc_config.py::TestVersionSpecificProperties`

**What it checks:**
- QLab 5 `customstring` not available in QLab 4
- QLab 4 `messagetype` not available in QLab 5
- Version-specific properties don't leak across versions

## Writing New Tests

### Test Structure

```python
import pytest
from osc_config import OSCConfig

class TestNewFeature:
    """Test description"""

    def test_feature_works(self):
        """Specific test case"""
        config = OSCConfig()
        result = config.some_method()
        assert result is not None
```

### Using Fixtures

```python
@pytest.fixture
def config():
    """Reusable OSC config"""
    return OSCConfig()

def test_with_fixture(config):
    assert config is not None
```

### Mocking External Dependencies

```python
from unittest.mock import Mock, patch

def test_with_mock():
    with patch('csv_parser.udp_client.UDPClient') as mock_client:
        mock_client.return_value = Mock()
        # Test code that uses UDP client
```

## Coverage Goals

| Module | Target | Current |
|--------|--------|---------|
| `osc_config.py` | 95%+ | 94% ✅ |
| `csv_parser.py` | 90%+ | 100% ✅ |
| `application.py` | 80%+ | 82% ✅ |
| Overall | 85%+ | 86% ✅ |

## Adding Tests for New Properties

When adding a new property to `qlab_osc_config.json`:

### 1. Add Validation Test

```python
def test_new_property_validation(config):
    """Test the new property validates correctly"""
    msg = config.build_osc_message('newproperty', 'valid_value')
    assert msg is not None

    msg = config.build_osc_message('newproperty', 'invalid_value')
    assert msg is None
```

### 2. Update Duplicate Detection Test

The duplicate detection test automatically checks all properties, so no changes needed if following naming conventions.

### 3. Add Type Conversion Test (if applicable)

```python
def test_new_property_type_conversion(config):
    """Test type conversion for new property"""
    # For int properties
    msg = config.build_osc_message('newproperty', '5')
    assert msg is not None
```

## Continuous Integration

Tests run automatically on GitHub Actions for:
- Pull requests
- Pushes to main branch
- Release workflows

### CI Configuration

See `.github/workflows/pytest.yml` for CI setup.

## Test Dependencies

From `requirements.txt`:
- `pytest>=8.0.0` - Testing framework
- `pytest-cov>=4.1.0` - Coverage reporting

## Common Test Patterns

### Testing Configuration Loading

```python
def test_config_loads():
    config = OSCConfig()
    assert config.global_properties is not None
    assert config.cue_type_properties is not None
```

### Testing OSC Message Building

```python
def test_build_message():
    config = OSCConfig()
    msg = config.build_osc_message('name', 'Test Cue')
    assert msg is not None
    built = msg.build()
    assert built is not None
```

### Testing CSV Parsing

```python
from unittest.mock import Mock, patch

def test_csv_parsing():
    with patch('csv_parser.udp_client.UDPClient') as mock_client:
        csv_content = MockFileStorage("Number,Type,Name\n1,audio,Test")
        send_csv('127.0.0.1', csv_content, 5, '')
        assert mock_client.return_value.send.called
```

## Debugging Failed Tests

### Verbose Output

```bash
python -m pytest -vv  # Extra verbose
python -m pytest -s   # Show print statements
```

### Run Single Test

```bash
python -m pytest app/tests/test_osc_config.py::test_name -vv
```

### Use pytest.set_trace() for Debugging

```python
def test_something():
    import pytest
    pytest.set_trace()  # Drops into debugger
    # Test code
```

## Test Coverage Reports

### Terminal Report

```bash
python -m pytest --cov=app --cov-report=term-missing
```

### HTML Report

```bash
python -m pytest --cov=app --cov-report=html
open htmlcov/index.html
```

### Coverage by Module

```bash
python -m pytest --cov=app --cov-report=term-missing | grep app/
```

## Best Practices

1. **Test behavior, not implementation** - Test what the code does, not how it does it
2. **Use descriptive test names** - `test_no_duplicate_property_names_global_vs_cue_specific` is better than `test_duplicates`
3. **One assertion per test** (when possible) - Makes failures easier to debug
4. **Mock external dependencies** - Don't make real network calls or file I/O in unit tests
5. **Test edge cases** - Empty strings, unicode, very long values, etc.
6. **Keep tests fast** - Mock slow operations, avoid sleep()

## Troubleshooting

### Import Errors

```bash
# Make sure you're in the project root
cd /path/to/csv_to_qlab

# Make sure virtual env is activated
source env/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Coverage Not Working

```bash
# Install coverage separately
pip install pytest-cov

# Check pytest plugins
python -m pytest --version
```

### Mocking Errors

```python
# Use correct import path
# ❌ Wrong: with patch('osc_config') as mock:
# ✅ Right: with patch('csv_parser.get_osc_config') as mock:
```

## See Also

- [Architecture Overview](./architecture.md) - System design
- [Adding Properties Guide](./adding-properties.md) - Extend configuration
- [OSC Configuration Schema](./osc-config-schema.md) - JSON structure
