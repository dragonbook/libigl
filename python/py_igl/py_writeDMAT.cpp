m.def("writeDMAT", []
(
  const std::string &str,
  const Eigen::MatrixXd& W
)
{
  igl::writeDMAT(str,W);
}, "Write dmat",
py::arg("str"), py::arg("W"));
