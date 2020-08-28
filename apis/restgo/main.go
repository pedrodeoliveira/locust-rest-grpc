package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"

	"github.com/go-playground/validator"
	"github.com/gorilla/mux"
	log "github.com/sirupsen/logrus"
)

const port int = 10000

// use a single instance of Validate, it caches struct info
var validate *validator.Validate

// TextCategorizationInput contains the input data received in a prediction request
type TextCategorizationInput struct {
	Text string `json:"text" validate:"required"`
}

// TextCategorizationOutput provides the output data returned in a prediction response
type TextCategorizationOutput struct {
	Text         string `json:"text"`
	PredictionID string `json:"prediction_id"`
	Category     int    `json:"category"`
}

// implements the /predict endpoint
func predict(w http.ResponseWriter, r *http.Request) {
	log.Debug("")
	body, err := ioutil.ReadAll(r.Body)
	if err != nil {
		log.Error(err)
	}

	var predictionInput TextCategorizationInput
	err = json.Unmarshal(body, &predictionInput)
	if err != nil {
		log.Error(err)
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	// perform validation of the unmarshalled struct
	err = validate.Struct(&predictionInput)
	if err != nil {
		log.Error(err)
		http.Error(w, err.Error(), http.StatusUnprocessableEntity)
		return
	}

	log.Infof("Received the following text to categorize: %s", predictionInput.Text)
	predictionOutput := TextCategorizationOutput{
		Text:         predictionInput.Text,
		PredictionID: "123",
		Category:     1,
	}

	// encode predictionOuput into JSON and send to ResponseWriter
	json.NewEncoder(w).Encode(predictionOutput)
}

func main() {
	address := fmt.Sprintf(":%d", port)
	log.Infof("Starting HTTP REST API at port %s ...", address)
	log.SetLevel(log.InfoLevel)

	// initialize validator
	validate = validator.New()

	// initialize router and add endpoints
	router := mux.NewRouter()
	router.HandleFunc("/predict", predict).Methods(http.MethodPost)

	// start http server
	log.Fatal(http.ListenAndServe(address, router))
}
