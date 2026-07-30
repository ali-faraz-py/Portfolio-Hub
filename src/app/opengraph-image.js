import { ImageResponse } from "next/og";

export const runtime = "edge";
export const alt = "Syed Ali Faraz — Machine Learning Engineer";
export const size = {
  width: 1200,
  height: 630,
};
export const contentType = "image/png";

export default async function Image() {
  return new ImageResponse(
    (
      <div
        style={{
          width: "100%",
          height: "100%",
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "flex-start",
          padding: "80px",
          backgroundColor: "#F7F6F3",
          fontFamily: "sans-serif",
        }}
      >
        <div
          style={{
            fontSize: 24,
            color: "#2955D6",
            letterSpacing: "0.1em",
            fontWeight: 700,
            marginBottom: 20,
          }}
        >
          MACHINE LEARNING ENGINEER
        </div>
        <div
          style={{
            fontSize: 56,
            color: "#14181C",
            fontWeight: 700,
            lineHeight: 1.1,
            maxWidth: 900,
          }}
        >
          I train models. Then I make them work for a living.
        </div>
        <div
          style={{
            fontSize: 22,
            color: "#6E7379",
            marginTop: 30,
          }}
        >
          Six deployed AI/ML projects — computer vision, NLP, classic ML
        </div>
      </div>
    ),
    {
      ...size,
    }
  );
}
