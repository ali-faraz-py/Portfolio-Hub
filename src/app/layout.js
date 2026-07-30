import { Space_Grotesk, JetBrains_Mono, Inter } from "next/font/google";
import "./globals.css";

const spaceGrotesk = Space_Grotesk({
  subsets: ["latin"],
  weight: ["500", "600", "700"],
  variable: "--font-display",
});

const jetbrainsMono = JetBrains_Mono({
  subsets: ["latin"],
  weight: ["400", "500", "600"],
  variable: "--font-mono",
});

const inter = Inter({
  subsets: ["latin"],
  weight: ["400", "500"],
  variable: "--font-body",
});

export const metadata = {
  metadataBase: new URL("https://portfolio-hub-dusky.vercel.app"),
  title: "Syed Ali Faraz — Machine Learning Engineer",
  description:
    "Portfolio of deployed AI/ML projects — computer vision, NLP, and classic ML systems built end-to-end.",
  openGraph: {
    title: "Syed Ali Faraz — Machine Learning Engineer",
    description:
      "Portfolio of deployed AI/ML projects — computer vision, NLP, and classic ML systems built end-to-end.",
    url: "https://portfolio-hub-dusky.vercel.app/",
    siteName: "Syed Ali Faraz Portfolio",
    type: "website",
  },
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body
        className={`${spaceGrotesk.variable} ${jetbrainsMono.variable} ${inter.variable} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}