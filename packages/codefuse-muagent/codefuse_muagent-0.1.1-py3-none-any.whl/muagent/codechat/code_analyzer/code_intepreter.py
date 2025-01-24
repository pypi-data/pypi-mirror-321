# encoding: utf-8
'''
@author: 温进
@file: code_intepreter.py
@time: 2023/11/22 上午11:57
@desc:
'''
from loguru import logger
from langchain.schema import (
    HumanMessage,
)

# from configs.model_config import CODE_INTERPERT_TEMPLATE
from muagent.base_configs.prompts import CODE_INTERPERT_TEMPLATE
from muagent.llm_models.openai_model import getChatModelFromConfig
from muagent.llm_models.llm_config import LLMConfig


class CodeIntepreter:
    def __init__(self, llm_config: LLMConfig):
        self.llm_config = llm_config

    def get_intepretation(self, code_list):
        '''
        get intepretion of code
        @param code_list:
        @return:
        '''
        # chat_model = getChatModel()
        chat_model = getChatModelFromConfig(self.llm_config)

        res = {}
        for code in code_list:
            message = CODE_INTERPERT_TEMPLATE.format(code=code)
            # message = [HumanMessage(content=message)]
            # chat_res = chat_model.predict_messages(message)
            # content = chat_res.content
            content = chat_model.predict(message)
            res[code] = content
        return res

    def get_intepretation_batch(self, code_list):
        '''
        get intepretion of code
        @param code_list:
        @return:
        '''
        # chat_model = getChatModel()
        chat_model = getChatModelFromConfig(self.llm_config)

        res = {}
        messages = []
        for code in code_list:
            message = CODE_INTERPERT_TEMPLATE.format(code=code)
            messages.append(message)

        try:
            chat_ress = [chat_model.predict(message) for message in messages]
        except Exception as e:
            logger.exception(f"{e}")
            chat_ress = chat_model.batch(messages)

        for chat_res, code in zip(chat_ress, code_list):
            try:
                res[code] = chat_res.content
            except:
                res[code] = chat_res
        return res




if __name__ == '__main__':
    engine = 'openai'
    code_list = ['''package com.theokanning.openai.client;
import com.theokanning.openai.DeleteResult;
import com.theokanning.openai.OpenAiResponse;
import com.theokanning.openai.audio.TranscriptionResult;
import com.theokanning.openai.audio.TranslationResult;
import com.theokanning.openai.billing.BillingUsage;
import com.theokanning.openai.billing.Subscription;
import com.theokanning.openai.completion.CompletionRequest;
import com.theokanning.openai.completion.CompletionResult;
import com.theokanning.openai.completion.chat.ChatCompletionRequest;
import com.theokanning.openai.completion.chat.ChatCompletionResult;
import com.theokanning.openai.edit.EditRequest;
import com.theokanning.openai.edit.EditResult;
import com.theokanning.openai.embedding.EmbeddingRequest;
import com.theokanning.openai.embedding.EmbeddingResult;
import com.theokanning.openai.engine.Engine;
import com.theokanning.openai.file.File;
import com.theokanning.openai.fine_tuning.FineTuningEvent;
import com.theokanning.openai.fine_tuning.FineTuningJob;
import com.theokanning.openai.fine_tuning.FineTuningJobRequest;
import com.theokanning.openai.finetune.FineTuneEvent;
import com.theokanning.openai.finetune.FineTuneRequest;
import com.theokanning.openai.finetune.FineTuneResult;
import com.theokanning.openai.image.CreateImageRequest;
import com.theokanning.openai.image.ImageResult;
import com.theokanning.openai.model.Model;
import com.theokanning.openai.moderation.ModerationRequest;
import com.theokanning.openai.moderation.ModerationResult;
import io.reactivex.Single;
import okhttp3.MultipartBody;
import okhttp3.RequestBody;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.*;
import java.time.LocalDate;
public interface OpenAiApi {
    @GET("v1/models")
    Single<OpenAiResponse<Model>> listModels();
    @GET("/v1/models/{model_id}")
    Single<Model> getModel(@Path("model_id") String modelId);
    @POST("/v1/completions")
    Single<CompletionResult> createCompletion(@Body CompletionRequest request);
    @Streaming
    @POST("/v1/completions")
    Call<ResponseBody> createCompletionStream(@Body CompletionRequest request);
    @POST("/v1/chat/completions")
    Single<ChatCompletionResult> createChatCompletion(@Body ChatCompletionRequest request);
    @Streaming
    @POST("/v1/chat/completions")
    Call<ResponseBody> createChatCompletionStream(@Body ChatCompletionRequest request);
    @Deprecated
    @POST("/v1/engines/{engine_id}/completions")
    Single<CompletionResult> createCompletion(@Path("engine_id") String engineId, @Body CompletionRequest request);
    @POST("/v1/edits")
    Single<EditResult> createEdit(@Body EditRequest request);
    @Deprecated
    @POST("/v1/engines/{engine_id}/edits")
    Single<EditResult> createEdit(@Path("engine_id") String engineId, @Body EditRequest request);
    @POST("/v1/embeddings")
    Single<EmbeddingResult> createEmbeddings(@Body EmbeddingRequest request);
    @Deprecated
    @POST("/v1/engines/{engine_id}/embeddings")
    Single<EmbeddingResult> createEmbeddings(@Path("engine_id") String engineId, @Body EmbeddingRequest request);
    @GET("/v1/files")
    Single<OpenAiResponse<File>> listFiles();
    @Multipart
    @POST("/v1/files")
    Single<File> uploadFile(@Part("purpose") RequestBody purpose, @Part MultipartBody.Part file);
    @DELETE("/v1/files/{file_id}")
    Single<DeleteResult> deleteFile(@Path("file_id") String fileId);
    @GET("/v1/files/{file_id}")
    Single<File> retrieveFile(@Path("file_id") String fileId);
    @Streaming
    @GET("/v1/files/{file_id}/content")
    Single<ResponseBody> retrieveFileContent(@Path("file_id") String fileId);
    @POST("/v1/fine_tuning/jobs")
    Single<FineTuningJob> createFineTuningJob(@Body FineTuningJobRequest request);
    @GET("/v1/fine_tuning/jobs")
    Single<OpenAiResponse<FineTuningJob>> listFineTuningJobs();
    @GET("/v1/fine_tuning/jobs/{fine_tuning_job_id}")
    Single<FineTuningJob> retrieveFineTuningJob(@Path("fine_tuning_job_id") String fineTuningJobId);
    @POST("/v1/fine_tuning/jobs/{fine_tuning_job_id}/cancel")
    Single<FineTuningJob> cancelFineTuningJob(@Path("fine_tuning_job_id") String fineTuningJobId);
    @GET("/v1/fine_tuning/jobs/{fine_tuning_job_id}/events")
    Single<OpenAiResponse<FineTuningEvent>> listFineTuningJobEvents(@Path("fine_tuning_job_id") String fineTuningJobId);
    @Deprecated
    @POST("/v1/fine-tunes")
    Single<FineTuneResult> createFineTune(@Body FineTuneRequest request);
    @POST("/v1/completions")
    Single<CompletionResult> createFineTuneCompletion(@Body CompletionRequest request);
    @Deprecated
    @GET("/v1/fine-tunes")
    Single<OpenAiResponse<FineTuneResult>> listFineTunes();
    @Deprecated
    @GET("/v1/fine-tunes/{fine_tune_id}")
    Single<FineTuneResult> retrieveFineTune(@Path("fine_tune_id") String fineTuneId);
    @Deprecated
    @POST("/v1/fine-tunes/{fine_tune_id}/cancel")
    Single<FineTuneResult> cancelFineTune(@Path("fine_tune_id") String fineTuneId);
    @Deprecated
    @GET("/v1/fine-tunes/{fine_tune_id}/events")
    Single<OpenAiResponse<FineTuneEvent>> listFineTuneEvents(@Path("fine_tune_id") String fineTuneId);
    @DELETE("/v1/models/{fine_tune_id}")
    Single<DeleteResult> deleteFineTune(@Path("fine_tune_id") String fineTuneId);
    @POST("/v1/images/generations")
    Single<ImageResult> createImage(@Body CreateImageRequest request);
    @POST("/v1/images/edits")
    Single<ImageResult> createImageEdit(@Body RequestBody requestBody);
    @POST("/v1/images/variations")
    Single<ImageResult> createImageVariation(@Body RequestBody requestBody);
    @POST("/v1/audio/transcriptions")
    Single<TranscriptionResult> createTranscription(@Body RequestBody requestBody);
    @POST("/v1/audio/translations")
    Single<TranslationResult> createTranslation(@Body RequestBody requestBody);
    @POST("/v1/moderations")
    Single<ModerationResult> createModeration(@Body ModerationRequest request);
    @Deprecated
    @GET("v1/engines")
    Single<OpenAiResponse<Engine>> getEngines();
    @Deprecated
    @GET("/v1/engines/{engine_id}")
    Single<Engine> getEngine(@Path("engine_id") String engineId);
    /**
     * Account information inquiry: It contains total amount (in US dollars) and other information.
     *
     * @return
     */
    @Deprecated
    @GET("v1/dashboard/billing/subscription")
    Single<Subscription> subscription();
    /**
     * Account call interface consumption amount inquiry.
     * totalUsage = Total amount used by the account (in US cents).
     *
     * @param starDate
     * @param endDate
     * @return Consumption amount information.
     */
    @Deprecated
    @GET("v1/dashboard/billing/usage")
    Single<BillingUsage> billingUsage(@Query("start_date") LocalDate starDate, @Query("end_date") LocalDate endDate);
}''', '''
package com.theokanning.openai;

/**
 * OkHttp Interceptor that adds an authorization token header
 * 
 * @deprecated Use {@link com.theokanning.openai.client.AuthenticationInterceptor}
 */
@Deprecated
public class AuthenticationInterceptor extends com.theokanning.openai.client.AuthenticationInterceptor {

    AuthenticationInterceptor(String token) {
        super(token);
    }

}
''']

    ci = CodeIntepreter(engine)
    res = ci.get_intepretation_batch(code_list)
    logger.debug(res)





