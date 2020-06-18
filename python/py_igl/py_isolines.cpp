m.def("isolines", []
(
  const Eigen::MatrixXd& V,
  const Eigen::MatrixXi& F,
  const Eigen::MatrixXd& z,
  const int n,
  Eigen::MatrixXd& isoV,
  Eigen::MatrixXi& isoE
)
{
  assert_is_VectorX("z",z);
  Eigen::VectorXd zz;
  if (z.size() != 0) zz = z;
  return igl::isolines(V, F, zz, n, isoV, isoE);
}, "isolines doc",
py::arg("V"), py::arg("F"), py::arg("z"), py::arg("n"), py::arg("isoV"), py::arg("isoE"));


m.def("isolines", []
(
  const Eigen::MatrixXd& V,
  const Eigen::MatrixXi& F,
  const Eigen::MatrixXd& z,
  const std::vector<double> &values,
  // const double s,
  Eigen::MatrixXd& isoV,
  Eigen::MatrixXi& isoE
)
{
  assert_is_VectorX("z",z);
  Eigen::VectorXd zz;
  if (z.size() != 0) zz = z;
  return igl::isolines(V, F, zz, values, isoV, isoE);
}, "isolines doc",
py::arg("V"), py::arg("F"), py::arg("values"), py::arg("s"), py::arg("isoV"), py::arg("isoE"));
