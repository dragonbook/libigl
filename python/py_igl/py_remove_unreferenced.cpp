m.def("remove_unreferenced", [] (
  const Eigen::MatrixXd& V,
  const Eigen::MatrixXi& F,
  Eigen::MatrixXd& NV,
  Eigen::MatrixXi& NF,
  Eigen::MatrixXi& I) {

  Eigen::VectorXi II;
  igl::remove_unreferenced(V, F, NV, NF, II);
  I = II;

}, "remove_unreferenced doc",
py::arg("V"), py::arg("F"), py::arg("NV"), py::arg("NF"), py::arg("I"));
