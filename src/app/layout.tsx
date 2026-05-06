import type { Metadata } from "next";
import { Inter, Playfair_Display } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"], variable: "--font-sans" });
const playfair = Playfair_Display({ subsets: ["latin"], variable: "--font-serif" });

export const metadata: Metadata = {
  title: 'CNX Cigars | Premium Cigar Lounge in Chiang Mai',
  description: 'Chiang Mai’s premier cigar lounge offering the largest collection of authentic Cuban and New World premium cigars in Northern Thailand.',
  keywords: 'Premium Cigars Chiang Mai, Cuban Cigars Thailand, Davidoff, Cohiba, Montecristo, Partagas, Romeo Y Julieta, Cigar Lounge Nimman, NPARC Chiang Mai, Buy Cigars Thailand, Luxury Lounge',
  openGraph: {
    title: 'CNX Cigars | Premium Cigar Lounge',
    description: 'Chiang Mai’s premier cigar lounge offering the largest collection of authentic Cuban and New World premium cigars in Northern Thailand.',
    url: 'https://cnxcigars.com',
    siteName: 'CNX Cigars',
    locale: 'en_US',
    type: 'website',
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${inter.variable} ${playfair.variable}`}>
        {children}
      </body>
    </html>
  );
}
