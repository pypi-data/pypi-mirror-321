#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <cstring>  // for memcpy
#include "simple_ans/cpp/simple_ans.hpp"

namespace py = pybind11;

// Template function to avoid code duplication in Python bindings
template <typename T>
void bind_ans_functions(py::module& m, const char* type_suffix)
{
    std::string encode_name = std::string("encode_") + type_suffix;
    std::string decode_name = std::string("decode_") + type_suffix;

    m.def(
        encode_name.c_str(),
        [](py::array_t<T> signal, py::array_t<uint32_t> symbol_counts, py::array_t<T> symbol_values)
        {
            py::buffer_info signal_buf = signal.request();
            py::buffer_info counts_buf = symbol_counts.request();
            py::buffer_info values_buf = symbol_values.request();

            if (counts_buf.ndim != 1 || values_buf.ndim != 1)
            {
                throw std::runtime_error("symbol_counts and symbol_values must be 1-dimensional");
            }
            if (counts_buf.shape[0] != values_buf.shape[0])
            {
                throw std::runtime_error(
                    "symbol_counts and symbol_values must have the same length");
            }

            return simple_ans::encode_t(static_cast<const T*>(signal_buf.ptr),
                                        signal_buf.size,
                                        static_cast<const uint32_t*>(counts_buf.ptr),
                                        static_cast<const T*>(values_buf.ptr),
                                        counts_buf.shape[0]);
        },
        "Encode signal using ANS",
        py::arg("signal").noconvert(),
        py::arg("symbol_counts").noconvert(),
        py::arg("symbol_values").noconvert());

    m.def(
        decode_name.c_str(),
        [](uint32_t state,
           const py::bytes& bitstream,
           size_t num_bits,
           py::array_t<uint32_t> symbol_counts,
           py::array_t<T> symbol_values,
           size_t n)
        {
            py::buffer_info counts_buf = symbol_counts.request();
            py::buffer_info values_buf = symbol_values.request();

            if (counts_buf.ndim != 1 || values_buf.ndim != 1)
            {
                throw std::runtime_error("symbol_counts and symbol_values must be 1-dimensional");
            }
            if (counts_buf.shape[0] != values_buf.shape[0])
            {
                throw std::runtime_error(
                    "symbol_counts and symbol_values must have the same length");
            }

            auto result = py::array_t<T>(n);
            py::buffer_info result_buf = result.request();

            // Convert bytes to uint64_t array
            std::string str = bitstream;
            const uint64_t* bitstream_ptr = reinterpret_cast<const uint64_t*>(str.data());

            simple_ans::decode_t(static_cast<T*>(result_buf.ptr),
                                 n,
                                 state,
                                 bitstream_ptr,
                                 num_bits,
                                 static_cast<const uint32_t*>(counts_buf.ptr),
                                 static_cast<const T*>(values_buf.ptr),
                                 counts_buf.shape[0]);

            return result;
        },
        "Decode ANS-encoded signal",
        py::arg("state"),
        py::arg("bitstream"),
        py::arg("num_bits"),
        py::arg("symbol_counts").noconvert(),
        py::arg("symbol_values").noconvert(),
        py::arg("n"));
}

PYBIND11_MODULE(_simple_ans, m)
{
    m.doc() = "Simple ANS (Asymmetric Numeral Systems) implementation";

    py::class_<simple_ans::EncodedData>(m, "EncodedData")
        .def(py::init<>())
        .def_readwrite("state", &simple_ans::EncodedData::state)
        .def_property("bitstream",
            [](const simple_ans::EncodedData& data) {
                // Convert vector<uint64_t> to bytes directly
                return py::bytes(reinterpret_cast<const char*>(data.bitstream.data()),
                               data.bitstream.size() * sizeof(uint64_t));
            },
            [](simple_ans::EncodedData& data, const py::bytes& bytes) {
                // Convert bytes back to vector<uint64_t>
                std::string str = bytes;
                data.bitstream.resize(str.size() / sizeof(uint64_t));
                std::memcpy(data.bitstream.data(), str.data(), str.size());
            })
        .def_readwrite("num_bits", &simple_ans::EncodedData::num_bits);

    // Bind signed and unsigned integer versions
    bind_ans_functions<int32_t>(m, "int32");
    bind_ans_functions<int16_t>(m, "int16");
    bind_ans_functions<uint32_t>(m, "uint32");
    bind_ans_functions<uint16_t>(m, "uint16");

    m.def(
        "choose_symbol_counts",
        [](py::array_t<double> proportions, uint32_t L)
        {
            py::buffer_info props_buf = proportions.request();
            if (props_buf.ndim != 1)
            {
                throw std::runtime_error("proportions must be 1-dimensional");
            }

            auto result = py::array_t<uint32_t>(props_buf.shape[0]);
            py::buffer_info result_buf = result.request();

            simple_ans::choose_symbol_counts(static_cast<uint32_t*>(result_buf.ptr),
                                             static_cast<const double*>(props_buf.ptr),
                                             props_buf.shape[0],
                                             L);

            return result;
        },
        "Convert real-valued proportions into integer counts summing to L",
        py::arg("proportions").noconvert(),
        py::arg("L"));
}
