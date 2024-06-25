-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Generation Time: Jun 25, 2024 at 07:59 PM
-- Server version: 10.6.17-MariaDB
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
--

-- --------------------------------------------------------

--
-- Table structure for table `destinos`
--

CREATE TABLE `destinos` (
  `id` int(11) NOT NULL,
  `titulo` varchar(45) NOT NULL,
  `descripcion` varchar(250) NOT NULL,
  `plan` varchar(45) NOT NULL,
  `preciofull` varchar(45) NOT NULL,
  `preciodes` varchar(45) NOT NULL,
  `favorito` varchar(45) NOT NULL,
  `foto` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `destinos`
--

INSERT INTO `destinos` (`id`, `titulo`, `descripcion`, `plan`, `preciofull`, `preciodes`, `favorito`, `foto`) VALUES
(1, 'Norte Argentino', 'Conocé los mejores cerros de Salta y Jujuy. Disfrutá de sus paisajes, su flora y fauna y la riquísima gastronomía regional.', '', '', '2', 'Si', 'UONLBXDWQIG2Z40_YE78.png'),
(2, 'Patagonia Argentina', 'Disfrutá de la gastronomía patagónica y recorré los paisajes mas emblemáticos de Rio Negro, Neuquén y Chubut.', '', '', '2', 'Si', 'P_MBAC6031G7VHEZ92JK.png'),
(3, 'Glariar Perito Moreno', 'Situado en Santa Cruz, en el Parque Nacional Los Glaciares, un lugar imponente por su inmensidad y belleza.', '', '', '2', 'No', 'PE4NR2G9CVFHQWMO_YX0.png'),
(4, 'Cataratas del Iguazu', 'Disfrutá de una de las maravillas del mundo. Recorre sus increíbles pasarelas y enamorate de cada rincón.', '', '', '2', 'No', '65Z8JMA2CXF1BRY90D_O.png');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `destinos`
--
ALTER TABLE `destinos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `destinos`
--
ALTER TABLE `destinos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
