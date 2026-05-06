import Foundation
import Vision
import Cocoa

guard CommandLine.arguments.count > 1 else {
    print("Usage: swift ocr.swift <image_path>")
    exit(1)
}

let imagePath = CommandLine.arguments[1]
guard let image = NSImage(contentsOfFile: imagePath),
      let cgImage = image.cgImage(forProposedRect: nil, context: nil, hints: nil) else {
    print("Failed to load image at \(imagePath)")
    exit(1)
}

let request = VNRecognizeTextRequest { (request, error) in
    guard let observations = request.results as? [VNRecognizedTextObservation] else {
        print("Failed to recognize text")
        return
    }
    for observation in observations {
        guard let candidate = observation.topCandidates(1).first else { continue }
        // CoreGraphics origin is bottom-left. Y goes 0 to 1.
        let y = observation.boundingBox.origin.y
        print("\(y)|\(candidate.string)")
    }
}
request.recognitionLevel = .accurate

let handler = VNImageRequestHandler(cgImage: cgImage, options: [:])
try? handler.perform([request])
